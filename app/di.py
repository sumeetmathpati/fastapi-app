from motor.motor_asyncio import AsyncIOMotorClient
from app.repository.app import AppsRepository
from app.repository.user import UserRepository
from kink import di
from app.core.config import Settings

di[Settings] = Settings()
di["MongoClient"] = lambda di: AsyncIOMotorClient(di[Settings].MONGO_DB_URL)
di[UserRepository] = lambda di: UserRepository(di["MongoClient"], di[Settings])
di[AppsRepository] = lambda di: AppsRepository(di["MongoClient"])

