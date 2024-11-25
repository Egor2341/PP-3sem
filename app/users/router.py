from typing import List

from fastapi import APIRouter, Response, Depends
from pydantic import EmailStr, parse_obj_as

from app.users.auth import get_password_hash, authenticate_user, create_access_token
import app.models as models
import app.service as service
import app.errors as errors

from db.users import User
from .dependencies import get_current_admin_user, get_current_user

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post("/register/", status_code=200)
def register_user(user_data: models.UserRegisterModel):
    user = service.get_user_by_email(user_data.email)
    if user:
        raise errors.user_already_exists()
    user_dict = user_data.dict()
    user_dict['password'] = get_password_hash(user_data.password)
    user_dict['role'] = user_dict['role'].value
    service.add_new_user(user_dict)


@router.post("/login/", status_code=200)
def auth_user(response: Response, user_data: models.UserAuthModel):
    user = authenticate_user(email=user_data.email, password=user_data.password)
    if user is None:
        raise errors.invalid_user()
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)

@router.post("/logout/", status_code=200)
def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")

@router.get("/all_users/", status_code=200)
def get_all_users(user_data: User = Depends(get_current_admin_user)) -> List[models.UserModel]:
    users = list(map(lambda obj: {"name": obj[0], "surname": obj[1], "email": obj[2]}, service.get_users(user_data.id)))
    return parse_obj_as(List[models.UserModel], users)

@router.delete("/ban_user/", status_code=200)
def ban_user(email_for_delete: EmailStr, user_data: User = Depends(get_current_admin_user)):
    service.delete_user(email_for_delete)


@router.post("/add_tour/", status_code=200)
def add_tour(tour_data: models.TourModel, user: User = Depends(get_current_admin_user)):
    tour = service.get_tour_by_title(tour_data.title)
    if tour:
        raise errors.tour_already_exists()
    service.add_new_tour(tour_data.dict())
