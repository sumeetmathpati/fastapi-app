from app.repository.mongo import AbstractMongoRepository, WriteMixin, SearchMixin

import abc

from motor.motor_asyncio import AsyncIOMotorClient
from app.schema.movie import MovieBase


class MovieRepository(AbstractMongoRepository, SearchMixin, WriteMixin):
    def __init__(self, client: AsyncIOMotorClient):
        db = client.get_database("movie_db")
        self.collection = db.get_collection("movie")
        self.model = MovieBase
        super().__init__(client=client)
