from typing import Annotated

from fastapi import APIRouter, Depends

from app.deps import current_user
from app.schema.user import UserBase
from app.view.api.routes.app import router as movies_router
from app.view.api.routes.users import router as users_router
from app.view.api.routes.auth import router as auth_router

router = APIRouter()

router.include_router(movies_router, prefix="/apps", tags=["apps"])
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])


@router.get("/")
async def home(user: Annotated[UserBase, Depends(current_user)]):
    return {"msg": f"Hello {user.name}"}
