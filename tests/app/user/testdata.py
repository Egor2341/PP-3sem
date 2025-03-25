from app.models import UserRegisterModel
from tests.testdata import REGISTER_DATA


USER_REGISTER_REQUEST_BODY = UserRegisterModel(**REGISTER_DATA).model_dump()
USER_REGISTER_REQUEST_BODY["role"] = "admin"
