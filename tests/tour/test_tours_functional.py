from starlette.testclient import TestClient

def test_get_all_tours(client: TestClient) -> None:
    resp = client.get("/tours/all_tours")
    assert resp.status_code == 200

def test_get_filtered_tours(client: TestClient) -> None:
    resp = client.get("/tours/filter_tours?title=ChinaTour")
    assert resp.status_code == 200