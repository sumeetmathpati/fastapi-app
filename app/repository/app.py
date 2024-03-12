from app.repository.mongo import AbstractMongoRepository, WriteMixin, SearchMixin

import abc

from motor.motor_asyncio import AsyncIOMotorClient
from app.schema.app import AppBase


class AppsRepository(AbstractMongoRepository, SearchMixin, WriteMixin):
    def __init__(self, client: AsyncIOMotorClient):
        db = client.get_database("poller")
        self.collection = db.get_collection("app")
        self.model = AppBase
        super().__init__(client=client)
