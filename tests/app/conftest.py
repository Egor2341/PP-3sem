import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.users.router import router as router_users
from app.tours.router import router as router_tours
from app.user_functional.router import router as router_funcs
from typing import Generator, Any


from db.database import Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

@pytest.fixture
def app() -> Generator[FastAPI, Any, None]:
    _app = FastAPI()
    _app.include_router(router_users)
    _app.include_router(router_tours)
    _app.include_router(router_funcs)
    yield _app

@pytest.fixture
def client(app) -> Generator[TestClient, Any, None]:
    _client = TestClient(app)
    yield _client
