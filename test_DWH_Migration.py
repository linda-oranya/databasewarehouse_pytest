import pytest
from main import DWH_Migration


@pytest.fixture(scope="module")
def connection_client():
    return DWH_Migration()


def test_connection_client():
    assert connection_client is not None


def test_get_stg_data(connection_client):
    data = connection_client.get_stg_data()
    assert data is not None


def test_get_prod_data(connection_client):
    data = connection_client.get_prod_data()
    assert data is not None


def test_data(connection_client):
    stg_data = connection_client.get_stg_data()
    prod_data = connection_client.get_prod_data()
    assert len(stg_data) == len(prod_data)
