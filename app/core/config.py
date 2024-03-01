import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    APP_NAME: str = "Fastapi APP"


settings = Settings()
