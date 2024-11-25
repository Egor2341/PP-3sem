from fastapi import APIRouter
from app.service import get_tours

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
