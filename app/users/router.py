from typing import List

from fastapi import APIRouter, Response, Depends
from pydantic import EmailStr, parse_obj_as

from app.users.auth import get_password_hash, authenticate_user, create_access_token
import app.models as models
import app.service as service
import app.errors as errors

from db.users import User
from .dependencies import get_current_admin_user, get_current_user, get_current_client_user

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


@router.delete("/remove_user/", status_code=200)
def remove_user(email_for_delete: EmailStr, user_data: User = Depends(get_current_admin_user)):
    service.delete_user(email_for_delete)


@router.post("/add_booking/", status_code=200)
def add_booking(number_of_people: int, tour_title: str, user_data: User = Depends(get_current_client_user)):
    tour = service.get_tour_by_title(tour_title)
    if tour is None or tour.availability < number_of_people:
        raise errors.tour_is_unavailable()
    booking_data = {}
    booking_data["number_of_people"] = number_of_people
    booking_data["total_price"] = tour.price * number_of_people
    booking_data["status"] = "unconfirmed"
    booking_data["user_id"] = user_data.id
    booking_data["tour_id"] = tour.id
    service.add_booking(booking_data)


@router.get("/all_bookings/", status_code=200)
def all_bookings(user_data: User = Depends(get_current_admin_user)) -> List[models.BookModel]:
    bookings = list(
        map(lambda b: {"id": b.id, "tour": service.get_tour_by_id(b.tour_id).title,
                       "user": service.get_user_by_id(b.user_id).email,
                       "number_of_people": b.number_of_people, "total_price": b.total_price, "status": b.status},
            service.get_all_bookings()))
    return parse_obj_as(List[models.BookModel], bookings)


@router.get("/user_bookings/", status_code=200)
def user_bookings(user_data: User = Depends(get_current_client_user)) -> List[models.BookModel]:
    bookings = list(
        map(lambda b: {"id": b.id, "tour": service.get_tour_by_id(b.tour_id).title,
                       "user": service.get_user_by_id(b.user_id).email,
                       "number_of_people": b.number_of_people, "total_price": b.total_price, "status": b.status},
            service.get_user_bookings(user_data.id)))
    return parse_obj_as(List[models.BookModel], bookings)


@router.put("/confirmation_booking/", status_code=200)
def confirmation_booking(booking_id: int, status: str, user_data: User = Depends(get_current_admin_user)):
    service.confirmation_booking(booking_id, status)


@router.put("/update_booking/", status_code=200)
def update_booking(booking_id: int, number_of_people: int, tour_title: str,
                   user_data: User = Depends(get_current_client_user)):
    tour = service.get_tour_by_title(tour_title)
    if tour is None or tour.availability < number_of_people:
        raise errors.tour_is_unavailable()
    booking_data = {}
    booking_data["number_of_people"] = number_of_people
    booking_data["total_price"] = tour.price * number_of_people
    booking_data["status"] = "unconfirmed"
    booking_data["user_id"] = user_data.id
    booking_data["tour_id"] = tour.id
    service.update_booking(booking_id, booking_data)


@router.delete("/remove_booking/", status_code=200)
def remove_booking(booking_id: int, user_data: User = Depends(get_current_user)):
    service.delete_booking(booking_id)


@router.post("/add_tour/", status_code=200)
def add_tour(tour_data: models.TourModel, user: User = Depends(get_current_admin_user)):
    tour = service.get_tour_by_title(tour_data.title)
    if tour:
        raise errors.tour_already_exists()
    tour_data.title = tour_data.title.lower()
    tour_data.destination = tour_data.destination.lower()
    service.add_new_tour(tour_data.dict())


@router.put("/update_tour/", status_code=200)
def update_tour(title: str, update_data: models.TourModel, user_data: User = Depends(get_current_admin_user)):
    update_data.title = update_data.title.lower()
    update_data.destination = update_data.destination.lower()
    service.update_tour(title, update_data.dict())


@router.delete("/remove_tour/", status_code=200)
def remove_tour(title: str, user_data: User = Depends(get_current_admin_user)):
    service.delete_tour(title)


@router.post("/add_review/", status_code=200)
def add_review(data: models.AddReviewModel, user_data: User = Depends(get_current_client_user)):
    review = {}
    review["user_id"] = user_data.id
    review["tour_id"] = service.get_tour_by_title(data.tour).id
    review["rating"] = data.rating
    review["comment"] = data.comment
    service.new_review(review)


@router.get("/all_reviews/", status_code=200)
def all_reviews(data_user: User = Depends(get_current_admin_user)) -> List[models.GetReviewModel]:
    reviews = service.get_all_reviews()
    result = list(
        map(lambda r: {"id": r.id, "tour": service.get_tour_by_id(r.tour_id).title,
                       "name": service.get_user_by_id(r.user_id).name,
                       "surname": service.get_user_by_id(r.user_id).surname, "rating": r.rating, "comment": r.comment},
            reviews))
    return parse_obj_as(List[models.GetReviewModel], result)


@router.get("/user_reviews/", status_code=200)
def user_reviews(data_user: User = Depends(get_current_client_user)) -> List[models.GetReviewModel]:
    reviews = service.get_user_reviews(data_user.id)
    user = service.get_user_by_id(data_user.id)
    result = list(
        map(lambda r: {"id": r.id, "tour": service.get_tour_by_id(r.tour_id).title,
                       "name": user.name, "surname": user.surname, "rating": r.rating, "comment": r.comment}, reviews))
    return parse_obj_as(List[models.GetReviewModel], result)


@router.put("/update_review/", status_code=200)
def update_review(old_comment: str, data: models.AddReviewModel, user_data: User = Depends(get_current_client_user)):
    review = {}
    review["user_id"] = user_data.id
    review["tour_id"] = service.get_tour_by_title(data.tour).id
    review["rating"] = data.rating
    review["comment"] = data.comment
    service.update_review(old_comment, review)


@router.delete("/delete_review/", status_code=200)
def delete_review(id: int, user_data: User = Depends(get_current_user)):
    service.delete_review(id)
