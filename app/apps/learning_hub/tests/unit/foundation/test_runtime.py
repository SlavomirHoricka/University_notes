from datetime import UTC, datetime
from uuid import UUID

import pytest
from learning_hub.application.core.runtime import SystemClock, UUIDGenerator
from learning_hub.domain.ports.runtime import Clock, IdGenerator


def test_runtime_ports_return_actual_time_and_distinct_ids() -> None:
    clock: Clock = SystemClock()
    ids: IdGenerator = UUIDGenerator()
    before = datetime.now(UTC)
    instant = clock.now()
    assert before <= instant <= datetime.now(UTC)
    assert instant.tzinfo == UTC
    first, second = ids.new("rec"), ids.new("rec")
    assert first != second
    assert UUID(first.removeprefix("rec_")).version == 4


@pytest.mark.parametrize("prefix", ["", "../../", "REC", "long"])
def test_invalid_id_prefix_rejected(prefix: str) -> None:
    with pytest.raises(ValueError):
        UUIDGenerator().new(prefix)
