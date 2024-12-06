import enum

from pydantic import BaseModel, EmailStr, Field
from decimal import Decimal
import datetime

class Role(enum.Enum):
    client = "client"
    admin = "admin"
class UserRegisterModel(BaseModel):
    name: str = Field(..., min_length=3, max_length=45, description="Имя, от 3 до 45 символов")
    surname: str = Field(..., min_length=3, max_length=45, description="Фамилия, от 3 до 45 символов")
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=8, max_length=50, description="Пароль, от 8 до 50 знаков")
    role: Role = Field(default=Role.client, description="Роль пользователя")

class UserAuthModel(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=6, max_length=50, description="Пароль, от 6 до 50 знаков")

class UserModel(BaseModel):
    name: str = Field(..., min_length=3, max_length=45, description="Имя, от 3 до 45 символов")
    surname: str = Field(..., min_length=3, max_length=45, description="Фамилия, от 3 до 45 символов")
    email: EmailStr = Field(..., description="Электронная почта")

class TourModel(BaseModel):
    title: str = Field(..., min_length=8, max_length=64, description="Название тура, от 8 до 64 символов")
    description: str = Field(..., min_length=30, max_length=500, description="Описание тура, от 30 до 500 символов")
    price: Decimal = Field(..., description="Стоимость поездки на одного человека")
    duration: int = Field(..., description="Продолжительность поездки в днях")
    start: datetime.datetime = Field(..., description="Дата начала")
    end: datetime.datetime = Field(..., description="Дата окончания")
    destination: str = Field(..., min_length=3, max_length=64, description="Место назначения")
    availability: int = Field(..., description="Количество доступных мест")

class BookModel(BaseModel):
    id: int = Field(..., description="Номер бронирования")
    tour: str = Field(..., min_length=8, max_length=64, description="Название тура, от 8 до 64 символов")
    user: EmailStr = Field(..., description="Электронная почта")
    number_of_people: int = Field(..., description="Количество человек")
    total_price: Decimal = Field(..., description="Общая стоимость")
    status: str = Field(..., description="Статус бронрования")
