import pytest

from sources.client.courier_support import (get_data_for_create_courier as new_data,
                                            delete_courier)


@pytest.fixture
def get_new_data():
    payload = new_data()
    yield payload
    delete_courier(payload)
