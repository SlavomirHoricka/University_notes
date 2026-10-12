from typing import get_args

import pytest
from learning_hub.domain.models.api import ErrorCode
from learning_hub.domain.ports.provider import (
    LOCAL_SESSION_COOKIE_NAME,
    LocalAuthorizationCode,
    LocalAuthorizationError,
)


@pytest.mark.parametrize("code", get_args(LocalAuthorizationCode))
def test_local_authorization_failure_has_exact_public_code_and_constant_message(
    code: LocalAuthorizationCode,
) -> None:
    error = LocalAuthorizationError(code)
    assert error.code == code and error.code in get_args(ErrorCode)
    assert str(error) and "token" not in str(error).lower()
    assert str(error) == str(LocalAuthorizationError(code))
    assert LOCAL_SESSION_COOKIE_NAME == "hub_session"
