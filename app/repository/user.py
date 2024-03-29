from app.core.config import Settings
from app.repository.mongo import AbstractMongoRepository, WriteMixin, SearchMixin
from fastapi.exceptions import HTTPException
from fastapi import status
from jose import JWTError, jwt
from motor.motor_asyncio import AsyncIOMotorClient

from app.schema.auth import EmailPassword
from app.schema.token import TokenData
from app.schema.user import UserBase, CreateUser, CreateUserDb, User, DbUser
from app.utils.auth import verify_password, get_password_hash
from pymongo.errors import DuplicateKeyError
from fastapi import status


class UserRepository(AbstractMongoRepository, SearchMixin, WriteMixin):
    def __init__(self, client: AsyncIOMotorClient, settings: Settings):
        db = client.get_database("poller")
        self.collection = db.get_collection("user")
        self.model = User
        self.settings = settings
        super().__init__(client=client)

    async def create_user(self, new_user: CreateUser) -> User:

        hashed_password = get_password_hash(new_user.password)
        db_user = CreateUserDb(**new_user.dict(), hashed_password=hashed_password)
        try:
            res = await self.create(db_user)
        except DuplicateKeyError as e:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="user with this email already exists."
            )
        return res

    async def authenticate_user(self, creds: EmailPassword) -> DbUser:
        user = await self.get_one(filters={"email": creds.email}, return_model=DbUser)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "user not found"})
        if not verify_password(creds.password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "invalid credentials"})
        return user

    async def get_current_user(self, token: str) -> User:
        """Get user from token"""
        try:
            payload = jwt.decode(token, self.settings.SECRET_KEY, algorithms=[self.settings.ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                return None
            token_data = TokenData(email=email)
        except JWTError:
            return None
        user = await self.get_one(filters={"email": token_data.email}, return_model=User)
        return user
