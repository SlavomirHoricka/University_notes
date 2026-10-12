import unicodedata
from typing import Annotated, Literal, Self

from pydantic import AfterValidator, StringConstraints, model_validator

from learning_hub.domain.models.base import (
    UUID4_PATTERN,
    BundleId,
    Contract,
    Digest,
    NonEmpty,
    PositiveInt,
    RelativePath,
    relative_path,
)


def course_path(value: str) -> str:
    relative_path(value)
    parts = value.split("/")
    if len(parts) != 3 or parts[1] not in ("Winter_Semester", "Summer_Semester"):
        raise ValueError("Full year/semester/course identity required")
    if parts[0] != "fixture":
        import re

        if not re.fullmatch(r"[0-9]{4}_[0-9]{4}", parts[0]):
            raise ValueError("Invalid academic year")
    return value


CourseId = Annotated[str, AfterValidator(course_path)]
CourseKey = Annotated[str, StringConstraints(pattern=r"^crs_[A-Za-z0-9_-]{8,64}$")]
ObjectiveId = Annotated[str, StringConstraints(pattern=r"^O[0-9]{3,}$")]
PlanVersion = Annotated[str, StringConstraints(pattern=r"^P[0-9]{3,}$")]
SourceVersion = Annotated[str, StringConstraints(pattern=r"^V[0-9]{3,}$")]


class CourseIdentity(Contract):
    course_id: CourseId
    academic_year: NonEmpty
    semester: Literal["Winter_Semester", "Summer_Semester"]
    course_folder: NonEmpty
    course_code: NonEmpty | None

    @model_validator(mode="after")
    def check_identity(self) -> Self:
        if self.course_id != f"{self.academic_year}/{self.semester}/{self.course_folder}":
            raise ValueError("Course identity must match exact folder spelling")
        return self


def assert_distinct_courses(courses: tuple[CourseIdentity, ...]) -> None:
    names = [unicodedata.normalize("NFC", course.course_id) for course in courses]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate or Unicode-equivalent course identities")


class VersionRef(Contract):
    course_id: CourseId
    plan_version: PlanVersion
    source_version: SourceVersion
    ingestion_revision: PositiveInt


class DefinitionRef(VersionRef):
    objective_id: ObjectiveId
    objective_revision: PositiveInt
    criterion_version: NonEmpty

    @model_validator(mode="after")
    def criterion_matches(self) -> Self:
        import re

        if not re.fullmatch(
            re.escape(self.objective_id) + r"-C[1-9][0-9]*", self.criterion_version
        ):
            raise ValueError("Criterion belongs to another objective")
        return self


class ItemRef(DefinitionRef):
    item_id: NonEmpty
    item_version: PositiveInt
    variant_id: Annotated[str, StringConstraints(pattern=r"^var_" + UUID4_PATTERN + r"$")]
    variant_version: PositiveInt


class BundleRef(VersionRef):
    bundle_id: BundleId
    bundle_schema_version: Literal[1] = 1
    public_digest: Digest
    private_digest: Digest


class AuthoringRef(Contract):
    id: NonEmpty
    revision: PositiveInt


class NoteLocator(Contract):
    path: RelativePath
    heading: NonEmpty
    block_id: NonEmpty | None = None


class CompatibilityRow(Contract):
    previous: DefinitionRef
    current: DefinitionRef
    classification: Literal["compatible", "requires_reassessment", "retired", "uncertain"]
    reason: NonEmpty

    @model_validator(mode="after")
    def same_course(self) -> Self:
        if self.previous.course_id != self.current.course_id:
            raise ValueError("Cross-course compatibility forbidden")
        return self
