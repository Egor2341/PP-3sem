from app.models import (UserRegisterModel,
                        UserAuthModel,
                        TourModel
)
from tests.testdata import (
    REGISTER_DATA,
    LOGIN_DATA,
    TOUR_DATA,
    TOUR_UPD_DATA,
    REGISTER_CLIENT_DATA,
    LOGIN_CLIENT_DATA
)


ADMIN_REGISTER_REQUEST_BODY = UserRegisterModel(**REGISTER_DATA).model_dump()
ADMIN_REGISTER_REQUEST_BODY["role"] = "admin"

ADMIN_LOGIN_REQUEST_BODY = UserAuthModel(**LOGIN_DATA).model_dump()

TOUR_REQUEST_BODY = TourModel(**TOUR_DATA).model_dump()
TOUR_REQUEST_BODY["price"] = 100000.00
TOUR_REQUEST_BODY["start"] = "2025-04-20 10:49"
TOUR_REQUEST_BODY["end"] = "2025-04-27"

TOUR_UPD_REQUEST_BODY = TourModel(**TOUR_UPD_DATA).model_dump()
TOUR_UPD_REQUEST_BODY["price"] = 100000.00
TOUR_UPD_REQUEST_BODY["start"] = "2025-04-20 10:49"
TOUR_UPD_REQUEST_BODY["end"] = "2025-04-27"

CLIENT_REGISTER_REQUEST_BODY = UserRegisterModel(**REGISTER_CLIENT_DATA).model_dump()
CLIENT_REGISTER_REQUEST_BODY["role"] = "client"

CLIENT_LOGIN_REQUEST_BODY = UserAuthModel(**LOGIN_CLIENT_DATA).model_dump()