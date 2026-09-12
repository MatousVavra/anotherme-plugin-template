import pytest


@pytest.fixture
def client(make_client):
    return make_client()


def test_hello_route(client):
    resp = client.get("/plugins/hello")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello from the AnotherMe plugin template!"}
