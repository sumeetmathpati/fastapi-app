from bson import ObjectId
from fastapi import APIRouter, HTTPException
from fastapi import Depends, Body, status
from fastapi import Request
from app.repository.app import AppsRepository
from app.repository.user import UserRepository
from app.schema.app import AppManyResponse, AppBase, AppIn, DbApp
from kink import di

from app.schema.user import User

router = APIRouter()


@router.get("/{app_id}", response_model=DbApp)
async def get_app(
        app_id: str,
        request: Request,
        repo: AppsRepository = Depends(lambda: di[AppsRepository]),
) -> DbApp:
    app: DbApp = await repo.get_one(filters={"_id": ObjectId(app_id), "ownerId": ObjectId(request.state.user.id)},
                                    return_model=DbApp)
    if not app:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="app not found"
        )
    return app


@router.get("", response_model=AppManyResponse)
async def get_apps(
        request: Request,
        repo: AppsRepository = Depends(lambda: di[AppsRepository]),
) -> AppManyResponse:
    """
    :return: List of movies
    """
    return await repo.get_many(filters={"ownerId": ObjectId(request.state.user.id)})


@router.post("", response_model=AppBase)
async def create_app(
        request: Request,
        app: AppIn = Body(),
        repo: AppsRepository = Depends(lambda: di[AppsRepository]),
) -> DbApp:
    record = app.model_dump(by_alias=True)
    record["ownerId"] = ObjectId(request.state.user.id)
    res = await repo.create(record, return_model=DbApp)
    return res
