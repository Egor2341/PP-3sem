from starlette.testclient import TestClient

from .testdata import(
    ADMIN_LOGIN_REQUEST_BODY,
    TOUR_REQUEST_BODY,
    TOUR_UPD_REQUEST_BODY,
    CLIENT_REGISTER_REQUEST_BODY,
    CLIENT_LOGIN_REQUEST_BODY
)


def test_get_users(client: TestClient) -> None:
    resp = client.get("/funcs/all_users/")
    assert resp.status_code == 401
    assert resp.json() == {"detail": "Invalid token"}

def test_add_tour(client: TestClient) -> None:
    client.post("/auth/login/", json=ADMIN_LOGIN_REQUEST_BODY)
    resp = client.post("/funcs/add_tour/", json=TOUR_REQUEST_BODY)
    assert resp.status_code == 200

def test_invalid_booking(client: TestClient) -> None:
    client.post("/auth/register/", json=CLIENT_REGISTER_REQUEST_BODY)
    client.post("/auth/login/", json=CLIENT_LOGIN_REQUEST_BODY)
    resp = client.post("/funcs/add_booking/?number_of_people=4&tour_title=ChinaTour")
    assert resp.status_code == 404
    assert resp.json() == {"detail": "Tour is unavailable"}

def test_update_tour(client: TestClient) -> None:
    client.post("/auth/login/", json=ADMIN_LOGIN_REQUEST_BODY)
    resp = client.put("/funcs/update_tour/?title=ChinaTour", json=TOUR_UPD_REQUEST_BODY)
    assert resp.status_code == 200

def test_remove_tour(client: TestClient) -> None:
    client.post("/auth/login/", json=ADMIN_LOGIN_REQUEST_BODY)
    resp = client.delete("/funcs/remove_tour/?title=ChinaTour")
    assert resp.status_code == 200


