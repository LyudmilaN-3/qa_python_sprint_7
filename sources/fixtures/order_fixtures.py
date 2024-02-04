import pytest

from sources.client.order_support import cancel_order


@pytest.fixture
def cansel_fix():
    payload = {}
    yield payload
    cancel_order(payload)
