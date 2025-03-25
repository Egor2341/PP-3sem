from starlette.testclient import TestClient

from .testdata import (
    ADMIN_REGISTER_REQUEST_BODY,
    ADMIN_LOGIN_REQUEST_BODY
)


def test_create_user(client: TestClient) -> None:
    resp = client.post("/auth/register/", json=ADMIN_REGISTER_REQUEST_BODY)
    assert resp.status_code == 200


def test_create_existed_user(client: TestClient) -> None:
    resp = client.post("/auth/register/", json=ADMIN_REGISTER_REQUEST_BODY)
    assert resp.status_code == 409
    assert resp.json() == {"detail": "The user already exists"}


def test_login_existed_user(client: TestClient) -> None:
    resp = client.post("/auth/login/", json=ADMIN_LOGIN_REQUEST_BODY)
    assert resp.status_code == 200
