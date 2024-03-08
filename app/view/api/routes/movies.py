from fastapi import APIRouter
from fastapi import Depends, Body

from app.repository.movie import MovieRepository
from app.schema.movie import MovieIn, MovieManyResponse, MovieBase
from kink import di

router = APIRouter()


@router.get("", response_model=MovieManyResponse)
async def get_movies(
        repo: MovieRepository = Depends(lambda: di[MovieRepository]),
):
    """
    :return: List of movies
    """
    return await repo.get_many()


@router.post("", response_model=MovieBase)
async def create_movie(
        movie: MovieIn = Body(),
        repo: MovieRepository = Depends(lambda: di[MovieRepository]),
):
    """
    :return: List of movies
    """
    res = await repo.create(movie)
    return res
