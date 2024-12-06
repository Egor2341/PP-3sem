from typing import Optional, List

from _decimal import Decimal
from fastapi import APIRouter

from app.service import get_tours, get_filtered_tours, get_tour_review, get_user_by_id

from pydantic import parse_obj_as

from app.models import TourModel, GetReviewModel

from app.errors import not_found

router = APIRouter(prefix='/tours', tags=['Tours'])


@router.get("/all_tours", status_code=200)
def get_all_tours() -> list[TourModel]:
    tours = list(
        map(lambda t: {"title": t.title, "description": t.description, "price": t.price, "duration": t.duration,
                       "start": t.start, "end": t.end, "destination": t.destination, "availability": t.availability},
            get_tours()))
    return parse_obj_as(list[TourModel], tours)


@router.get("/filter_tours", status_code=200)
def filter_tours(title: Optional[str] = None, price: Optional[Decimal] = None, duration: Optional[int] = None,
                 destination: Optional[str] = None, number_of_peoples: Optional[int] = None) -> list[TourModel]:
    tours = list(
        map(lambda t: {"title": t.title, "description": t.description, "price": t.price, "duration": t.duration,
                       "start": t.start, "end": t.end, "destination": t.destination, "availability": t.availability},
            get_filtered_tours(title, price, duration, destination, number_of_peoples)))
    return parse_obj_as(list[TourModel], tours)


@router.get("/tour_reviews", status_code=200)
def tour_reviews(title: str) -> List[GetReviewModel]:
    reviews = get_tour_review(title)
    if reviews is None:
        raise not_found()
    result = list(
        map(lambda r: {"id": r.id, "tour": title,
                       "name": get_user_by_id(r.user_id).name, "surname": get_user_by_id(r.user_id).surname,
                       "rating": r.rating, "comment": r.comment}, reviews))
    return parse_obj_as(List[GetReviewModel], result)
