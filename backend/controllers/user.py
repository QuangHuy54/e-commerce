from uuid import UUID
from fastapi import APIRouter

from models.user import UserModel
from repositories.user import get_user


router = APIRouter()


@router.get("/get", status_code=200, tags=["User"], description="Get user information")
async def get(id: UUID) -> UserModel:
    user = get_user(id)
    return user
