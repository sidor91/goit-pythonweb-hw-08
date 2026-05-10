from fastapi import APIRouter, Depends
from src.database.users.schemas import User
from src.auth.service import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=User)
async def me(user: User = Depends(get_current_user)):
    return user
