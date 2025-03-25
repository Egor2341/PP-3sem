from starlette.testclient import TestClient

from .testdata import(
    USER_REGISTER_REQUEST_BODY
)

def test_create_user(client: TestClient) -> None:
    resp = client.post("/auth/register/", json=USER_REGISTER_REQUEST_BODY)
    assert resp.status_code == 200

def test_create_existed_user(client: TestClient) -> None:
    resp = client.post("/auth/register/", json=USER_REGISTER_REQUEST_BODY)
    assert resp.status_code == 409


