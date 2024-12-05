from typing import Annotated
from fastapi import Path,APIRouter

router=APIRouter(prefix="/items",tags=['Items'])

@router.get('/')
def get_items():
    return [
        'item_1',
        'item_2'
    ]

@router.get('/latest/')
def get_latest_items():
    return {'data': {'latest': 23}}

@router.get('/{item_id}/')
def get_items_by_id(item_id: Annotated[int,Path(ge=1,lt=100000)]):
    return {
        "item": {"id": item_id}
    }