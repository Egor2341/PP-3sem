from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone

from pydantic import EmailStr

from app.config import get_auth_data
from db.database import session_factory
from db.users import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
    return encode_jwt

def authenticate_user(email: EmailStr, password: str):
    with session_factory() as session:
        user = session.query(User).filter(User.email == email).first()
        if not user or verify_password(plain_password=password, hashed_password=user.password) is False:
            return None
        return user
