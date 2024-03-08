from app.repository.mongo import AbstractMongoRepository, WriteMixin, SearchMixin

import abc

from motor.motor_asyncio import AsyncIOMotorClient
from app.schema.review import ReviewBase


class ReviewRepository(AbstractMongoRepository, SearchMixin, WriteMixin):
    def __init__(self, client: AsyncIOMotorClient):
        db = client.get_database("movie_db")
        self.collection = db.get_collection("review")
        self.model = ReviewBase
        super().__init__(client=client)
