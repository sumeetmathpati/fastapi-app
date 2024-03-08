from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict

from app.schema.mongo import PyObjectId


class MovieBase(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class MovieIn(BaseModel):
    title: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class MovieManyResponse(BaseModel):
    records: List[MovieBase]