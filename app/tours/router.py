from typing import Optional

from _decimal import Decimal
from fastapi import APIRouter
from app.service import get_tours, get_filtered_tours

from pydantic import parse_obj_as

from app.models import TourModel

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
