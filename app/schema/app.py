from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict

from app.schema.app_configs import OutlookConfig
from app.schema.mongo import PyObjectId
from enum import Enum, IntEnum


class AppType(str, Enum):
    outlook = 'outlook'


class AppBase(BaseModel):
    owner_id: Optional[PyObjectId] = Field(alias="ownerId", default=None)
    name: str
    type: AppType
    config: OutlookConfig
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class AppIn(BaseModel):
    name: str = Field(...)
    type: AppType
    config: OutlookConfig
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class DbApp(AppBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )

class AppManyResponse(BaseModel):
    records: List[DbApp]
