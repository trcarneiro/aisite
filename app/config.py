import logging
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SESSION_SECRET: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f"SECRET_KEY loaded: {settings.SESSION_SECRET}")
