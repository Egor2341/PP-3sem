from typing import List

from fastapi import Depends, APIRouter
from pydantic import parse_obj_as, EmailStr
from pydantic import TypeAdapter

from db.bookings import Booking
from db.reviews import Review
from db.tours import Tour
from db.users import User
from .dependencies import get_current_admin_user, get_current_user, get_current_client_user
from app import models, errors
from app.services import service, user_service, tour_service, booking_service, review_service

router = APIRouter(prefix='/funcs', tags=['Funcs'])


@router.get("/all_users/", status_code=200)
def get_all_users(user_data: User = Depends(get_current_admin_user)) -> List[models.UserModel]:
    users = list(
        map(lambda obj: {"name": obj[0], "surname": obj[1], "email": obj[2]}, user_service.get_users(user_data.id)))
    return TypeAdapter(List[models.UserModel]).validate_python(users)


@router.delete("/remove_user/", status_code=200)
def remove_user(email_for_delete: EmailStr, user_data: User = Depends(get_current_admin_user)):
    user_service.delete_user(email_for_delete)


@router.post("/add_booking/", status_code=200)
def add_booking(number_of_people: int, tour_title: str, user_data: User = Depends(get_current_client_user)):
    tour = tour_service.get_tour_by_title(tour_title)
    if tour is None or tour.availability < number_of_people:
        raise errors.tour_is_unavailable()
    booking_data = {}
    booking_data["number_of_people"] = number_of_people
    booking_data["total_price"] = tour.price * number_of_people
    booking_data["status"] = "unconfirmed"
    booking_data["user_id"] = user_data.id
    booking_data["tour_id"] = tour.id
    booking_service.add_booking(booking_data)


@router.get("/all_bookings/", status_code=200)
def all_bookings(user_data: User = Depends(get_current_admin_user)) -> List[models.BookModel]:
    bookings = list(
        map(lambda b: {"id": b.id, "tour": service.get_by_id(Tour, b.tour_id).title,
                       "user": service.get_by_id(User, b.user_id).email,
                       "number_of_people": b.number_of_people, "total_price": b.total_price, "status": b.status},
            service.get_all(Booking)))
    return TypeAdapter(List[models.BookModel]).validate_python(bookings)


@router.get("/user_bookings/", status_code=200)
def user_bookings(user_data: User = Depends(get_current_client_user)) -> List[models.BookModel]:
    bookings = list(
        map(lambda b: {"id": b.id, "tour": service.get_by_id(Tour, b.tour_id).title,
                       "user": service.get_by_id(User, b.user_id).email,
                       "number_of_people": b.number_of_people, "total_price": b.total_price, "status": b.status},
            booking_service.get_user_bookings(user_data.id)))
    return TypeAdapter(List[models.BookModel]).validate_python(bookings)


@router.put("/confirmation_booking/", status_code=200)
def confirmation_booking(booking_id: int, status: str, user_data: User = Depends(get_current_admin_user)):
    booking_service.confirmation_booking(booking_id, status)


@router.put("/update_booking/", status_code=200)
def update_booking(booking_id: int, number_of_people: int, tour_title: str,
                   user_data: User = Depends(get_current_client_user)):
    tour = tour_service.get_tour_by_title(tour_title)
    if tour is None or tour.availability < number_of_people:
        raise errors.tour_is_unavailable()
    booking_data = {}
    booking_data["number_of_people"] = number_of_people
    booking_data["total_price"] = tour.price * number_of_people
    booking_data["status"] = "unconfirmed"
    booking_data["user_id"] = user_data.id
    booking_data["tour_id"] = tour.id

    booking_service.update_booking(booking_id, booking_data)


@router.delete("/remove_booking/", status_code=200)
def remove_booking(booking_id: int, user_data: User = Depends(get_current_user)):
    booking_service.delete_booking(booking_id)


@router.post("/add_tour/", status_code=200)
def add_tour(tour_data: models.TourModel, user: User = Depends(get_current_admin_user)):
    tour = tour_service.get_tour_by_title(tour_data.title)
    if tour:
        raise errors.tour_already_exists()
    tour_data.title = tour_data.title.lower()
    tour_data.destination = tour_data.destination.lower()
    service.add_new_row(Tour, tour_data.model_dump())


@router.put("/update_tour/", status_code=200)
def update_tour(title: str, update_data: models.TourModel, user_data: User = Depends(get_current_admin_user)):
    update_data.title = update_data.title.lower()
    update_data.destination = update_data.destination.lower()
    tour_service.update_tour(title, update_data.model_dump())


@router.delete("/remove_tour/", status_code=200)
def remove_tour(title: str, user_data: User = Depends(get_current_admin_user)):
    tour_service.delete_tour(title.lower())


@router.post("/add_review/", status_code=200)
def add_review(data: models.AddReviewModel, user_data: User = Depends(get_current_client_user)):
    review = {}
    review["user_id"] = user_data.id
    review["tour_id"] = tour_service.get_tour_by_title(data.tour).id
    review["rating"] = data.rating
    review["comment"] = data.comment
    review_service.new_review(review)


@router.get("/all_reviews/", status_code=200)
def all_reviews(data_user: User = Depends(get_current_admin_user)) -> List[models.GetReviewModel]:
    reviews = service.get_all(Review)
    result = list(
        map(lambda r: {"id": r.id, "tour": service.get_by_id(Tour, r.tour_id).title,
                       "name": service.get_by_id(User, r.user_id).name,
                       "surname": service.get_by_id(User, r.user_id).surname, "rating": r.rating, "comment": r.comment},
            reviews))
    return TypeAdapter(List[models.GetReviewModel]).validate_python(result)


@router.get("/user_reviews/", status_code=200)
def user_reviews(data_user: User = Depends(get_current_client_user)) -> List[models.GetReviewModel]:
    reviews = review_service.get_user_reviews(data_user.id)
    user = service.get_by_id(User, data_user.id)
    result = list(
        map(lambda r: {"id": r.id, "tour": service.get_by_id(Tour, r.tour_id).title,
                       "name": user.name, "surname": user.surname, "rating": r.rating, "comment": r.comment}, reviews))
    return TypeAdapter(List[models.GetReviewModel]).validate_python(result)


@router.put("/update_review/", status_code=200)
def update_review(old_comment: str, data: models.AddReviewModel, user_data: User = Depends(get_current_client_user)):
    review = {}
    review["user_id"] = user_data.id
    review["tour_id"] = tour_service.get_tour_by_title(data.tour).id
    review["rating"] = data.rating
    review["comment"] = data.comment
    review_service.update_review(old_comment, review)


@router.delete("/delete_review/", status_code=200)
def delete_review(id: int, user_data: User = Depends(get_current_user)):
    review_service.delete_review(id)
