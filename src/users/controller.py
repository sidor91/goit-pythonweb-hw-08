from fastapi import APIRouter, Depends, Request
from src.database.users.schemas import User
from src.auth.service import get_current_user
from src.utils.limiter import limiter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=User)
@limiter.limit("5/minute")  # type: ignore
async def me(request: Request, user: User = Depends(get_current_user)):
    return user
