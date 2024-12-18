from app.errors import invalid_user, invalid_token, access_is_denied
from fastapi import Request, Depends
from app.config import get_auth_data
from jose import jwt, JWTError

from app.service import get_user_by_id
from db.users import User


def get_token(request: Request):
    token = request.cookies.get('users_access_token')
    if not token:
        raise invalid_token()
    return token


def get_current_user(token: str = Depends(get_token)):
    try:
        auth_data = get_auth_data()
        payload = jwt.decode(token, auth_data['secret_key'], algorithms=[auth_data['algorithm']])
    except JWTError:
        raise invalid_token()

    user_id = payload.get('sub')
    if not user_id:
        raise invalid_user()

    user = get_user_by_id(int(user_id))
    if not user:
        raise invalid_user()
    return user


def get_current_client_user(current_user: User = Depends(get_current_user)):
    if current_user.role == "client":
        return current_user
    raise access_is_denied()


def get_current_admin_user(current_user: User = Depends(get_current_user)):
    if current_user.role == "admin":
        return current_user
    raise access_is_denied()
