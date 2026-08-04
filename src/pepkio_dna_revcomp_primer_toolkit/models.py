"""Typed API request/response models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict

from .exceptions import PepkioAPIError


class RunOptions(BaseModel):
    """Optional execution options for POST .../run."""

    idempotency_key: str | None = None
    label: str | None = None


class RunResult(BaseModel):
    """Tool run response envelope."""

    model_config = ConfigDict(extra="allow")

    run_id: str
    status: str
    result: dict[str, Any] | None = None
    error: Any | None = None
    result_url: str | None = None
    permalink: str | None = None
    duration_ms: int | None = None

    def raise_for_error(self) -> None:
        """Raise PepkioAPIError if the response contains an error."""
        if self.error is None:
            return
        if isinstance(self.error, dict):
            err = self.error
            msg = err.get("message") or "Tool run failed"
            code = err.get("code")
            details = err.get("details") if isinstance(err.get("details"), dict) else {}
        elif isinstance(self.error, str):
            msg = self.error
            code = "TOOL_ERROR"
            details = {}
        else:
            msg = str(self.error)
            code = "TOOL_ERROR"
            details = {}

        raise PepkioAPIError(
            msg,
            code=code,
            details=details,
            response_body={"run_id": self.run_id, "status": self.status, "error": self.error},
        )


def parse_run_response(data: dict[str, Any]) -> RunResult:
    """Parse a run API JSON response into a RunResult."""
    return RunResult.model_validate(data)
