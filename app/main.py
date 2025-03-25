from fastapi import FastAPI
from app.users.router import router as router_users
from app.tours.router import router as router_tours
from app.user_functional.router import router as router_funcs
import __init__


app = FastAPI()


@app.get("/", status_code=200)
def home_page():
    return


app.include_router(router_users)
app.include_router(router_tours)
app.include_router(router_funcs)

