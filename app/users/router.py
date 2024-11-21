from fastapi import APIRouter, HTTPException, status
from app.users.auth import get_password_hash
from app.users.models import UserRegisterModel
from db.database import session_factory
from db.users import User
import app.errors as errors

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post("/register/", status_code=200)
def register_user(user_data: UserRegisterModel):
    with session_factory() as session:
        user = session.query(User).filter(User.email == user_data.email).first()
        if user:
            raise errors.user_is_not_on_project()
        user_dict = user_data.dict()
        user_dict['password'] = get_password_hash(user_data.password)
        user_dict['role'] = user_dict['role'].value
        session.add(User(**user_dict))
        session.commit()
