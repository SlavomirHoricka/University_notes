import hashlib
import json
from collections.abc import Iterable
from datetime import datetime
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import PurePosixPath
from typing import Annotated

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, StringConstraints


class Contract(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)


PositiveInt = Annotated[int, Field(ge=1)]
NonNegativeInt = Annotated[int, Field(ge=0)]
NonEmpty = Annotated[str, StringConstraints(min_length=1, max_length=500)]
Digest = Annotated[str, StringConstraints(pattern=r"^[0-9a-f]{64}$")]
GitCommit = Annotated[str, StringConstraints(pattern=r"^[0-9a-f]{40}$")]
UUID4_PATTERN = r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
OperationalId = Annotated[str, StringConstraints(pattern=r"^[a-z]{3}_" + UUID4_PATTERN + r"$")]


def prefixed_id(prefix: str) -> object:
    return StringConstraints(pattern="^" + prefix + "_" + UUID4_PATTERN + "$")


SessionId = Annotated[str, prefixed_id("ses")]
AttemptId = Annotated[str, prefixed_id("att")]
DeliveryId = Annotated[str, prefixed_id("del")]
ReceiptId = Annotated[str, prefixed_id("rec")]
BundleId = Annotated[str, prefixed_id("pub")]
JobId = Annotated[str, prefixed_id("job")]
CommandId = Annotated[str, prefixed_id("cmd")]


def aware_time(value: str) -> str:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError("Invalid ISO-8601 instant") from error
    if parsed.utcoffset() is None:
        raise ValueError("Offset-aware instant required")
    return value


def utc_time(value: str) -> str:
    aware_time(value)
    if not value.endswith("Z"):
        raise ValueError("Server instant must end in Z")
    return value


ReportedTime = Annotated[str, AfterValidator(aware_time)]
UTCTime = Annotated[str, AfterValidator(utc_time)]


def relative_path(value: str) -> str:
    path = PurePosixPath(value)
    if (
        not value
        or path.is_absolute()
        or "\\" in value
        or "\x00" in value
        or any(part in ("", ".", "..") for part in value.split("/"))
    ):
        raise ValueError("Safe relative POSIX path required")
    return value


RelativePath = Annotated[str, AfterValidator(relative_path)]


def decimal_string(value: str, *, significant_digits: int = 50) -> str:
    if len(value) > 128:
        raise ValueError("Decimal input is too long")
    import re

    if not re.fullmatch(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?", value):
        raise ValueError("Base-10 decimal string required")
    try:
        parsed = Decimal(value)
    except InvalidOperation as error:
        raise ValueError("Invalid decimal") from error
    if not parsed.is_finite() or len(parsed.as_tuple().digits) > significant_digits:
        raise ValueError(
            f"Finite decimal with at most {significant_digits} significant digits required"
        )
    return value


def nonnegative_decimal(value: str) -> str:
    decimal_string(value)
    if Decimal(value) < 0:
        raise ValueError("Nonnegative decimal required")
    return value


DecimalString = Annotated[str, AfterValidator(decimal_string)]
Points = Annotated[str, AfterValidator(nonnegative_decimal)]


def canonical_json(value: Contract) -> bytes:
    return json.dumps(
        value.model_dump(mode="json"),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def contract_digest(value: Contract) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def decimal_sum(values: Iterable[str]) -> Decimal:
    with localcontext() as context:
        context.prec = 80
        return sum((Decimal(value) for value in values), Decimal(0))


def decimal_weight_between(amount: Decimal, total: Decimal, lower: str, upper: str) -> bool:
    with localcontext() as context:
        context.prec = 80
        return total * Decimal(lower) <= amount <= total * Decimal(upper)


def calculated_decimal(value: str) -> str:
    """Server-derived precision-80 Decimal; learner numeric input remains limited to 50 digits."""
    decimal_string(value, significant_digits=80)
    if Decimal(value) < 0:
        raise ValueError("Nonnegative calculated decimal required")
    return value


CalculatedDecimal = Annotated[str, AfterValidator(calculated_decimal)]
