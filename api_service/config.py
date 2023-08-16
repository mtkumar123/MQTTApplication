from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Read in environment variables
    """

    mongo_db_url: str
    mongo_db_port: int
    db_name: str
    collection_name: str


@lru_cache
def get_settings():
    return Settings()
