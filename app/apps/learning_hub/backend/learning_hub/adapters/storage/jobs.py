import json
import sqlite3

from learning_hub.domain.models.services import JobViewV1, RequestedJobV1


class JobConflict(ValueError):
    pass


class SQLiteRequestedJobs:
    """H07 can persist requested work before H08 supplies worker execution."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def get(self, job_id: str) -> JobViewV1 | None:
        row = self.connection.execute("SELECT * FROM jobs WHERE job_id=?", (job_id,)).fetchone()
        if row is None:
            return None
        request = {
            "job_id": row["job_id"],
            "course_key": row["course_key"],
            "kind": row["kind"],
            "dedupe_key": row["dedupe_key"],
            "input_ref": json.loads(row["input_ref"]),
            "requested_settings": json.loads(row["requested_settings"]),
            "created_at": row["created_at"],
        }
        return JobViewV1.model_validate_json(
            json.dumps(
                {
                    "request": request,
                    "state": row["state"],
                    "revision": row["revision"],
                    "actual_settings": json.loads(row["actual_settings"])
                    if row["actual_settings"]
                    else None,
                    "next_eligible_at": row["next_eligible_at"],
                    "error_code": json.loads(row["error"]).get("code") if row["error"] else None,
                }
            )
        )

    def request(self, request: RequestedJobV1) -> JobViewV1:
        self.connection.execute("BEGIN IMMEDIATE")
        try:
            existing = self.connection.execute(
                "SELECT job_id FROM jobs WHERE dedupe_key=?", (request.dedupe_key,)
            ).fetchone()
            if existing:
                view = self.get(existing["job_id"])
                if view is None:
                    raise JobConflict("Requested job disappeared")
                if (
                    view.request.course_key,
                    view.request.kind,
                    view.request.input_ref,
                    view.request.requested_settings,
                ) != (
                    request.course_key,
                    request.kind,
                    request.input_ref,
                    request.requested_settings,
                ):
                    raise JobConflict("Job dedupe key reused for different request")
                self.connection.commit()
                return view
            self.connection.execute(
                "INSERT INTO "
                "jobs(job_id,course_key,kind,dedupe_key,input_ref,requested_settings,"
                "state,revision,created_at) VALUES(?,?,?,?,?,?,'queued',1,?)",
                (
                    request.job_id,
                    request.course_key,
                    request.kind,
                    request.dedupe_key,
                    request.input_ref.model_dump_json(),
                    request.requested_settings.model_dump_json(),
                    request.created_at,
                ),
            )
            self.connection.commit()
        except BaseException:
            self.connection.rollback()
            raise
        view = self.get(request.job_id)
        if view is None:
            raise JobConflict("Requested job was not persisted")
        return view
