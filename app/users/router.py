from fastapi import APIRouter, HTTPException, status
from app.users.auth import get_password_hash
from app.users.models import UserRegisterModel
from data_base.database import session_factory
from data_base.users import User

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post("/register/")
def register_user(user_data: UserRegisterModel) -> dict:
    with session_factory() as session:
        user = session.query(User).filter(User.email == user_data.email).first()
        if user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Пользователь уже существует'
            )
        user_dict = user_data.dict()
        user_dict['password'] = get_password_hash(user_data.password)
        session.add(User(**user_dict))
        session.commit()
    return {'message': 'Вы успешно зарегистрированы!'}