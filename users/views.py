from fastapi import APIRouter
from users.schemas import CreateUser
from users import crud

router=APIRouter(prefix='/users',tags=["Users"])

@router.post('/')
def user(user:CreateUser):
    return crud.create_user(user_in=user)