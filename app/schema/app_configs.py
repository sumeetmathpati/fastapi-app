from typing import Optional

from pydantic import BaseModel, Field


class CronDetail(BaseModel):
    sec: int
    min: int
    hr: int
    month_day: int = Field(..., alias="monthDay")
    month: int
    week_day: int = Field(..., alias="weekDay")
    year: Optional[int]

class ScheduleDetails(BaseModel):
    cron: Optional[CronDetail]


class AppConfig(BaseModel):
    schedule_details: Optional[ScheduleDetails] = Field(None, alias="scheduleDetails")


class OutlookConfig(AppConfig):
    tenant_id: str = Field(alias="tenantId")
    client_id: str = Field(alias="clientId")
    secret: str = Field(alias="secret")
