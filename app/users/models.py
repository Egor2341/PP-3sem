import enum

from pydantic import BaseModel, EmailStr, Field

class Role(enum.Enum):
    client = "client"
    admin = "admin"
class UserRegisterModel(BaseModel):
    name: str = Field(..., min_length=3, max_length=45, description="Имя, от 3 до 45 символов")
    surname: str = Field(..., min_length=3, max_length=45, description="Фамилия, от 3 до 45 символов")
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=8, max_length=50, description="Пароль, от 8 до 50 знаков")
    role: Role = Field(default=Role.client, description="Роль пользователя")


