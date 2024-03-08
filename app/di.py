from motor.motor_asyncio import AsyncIOMotorClient
from app.repository.movie import MovieRepository
from app.repository.review import ReviewRepository
from app.repository.user import UserRepository
from kink import di
from app.core.config import Settings

di[Settings] = Settings()
di["MongoClient"] = lambda di: AsyncIOMotorClient(di[Settings].MONGO_DB_URL)
di[UserRepository] = lambda di: UserRepository(di["MongoClient"], di[Settings])
di[ReviewRepository] = lambda di: ReviewRepository(di["MongoClient"])
di[MovieRepository] = lambda di: MovieRepository(di["MongoClient"])

