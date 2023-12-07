from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker

from app.api.dependencies.database import DbProvider, dao_provider
from app.api.dependencies.settings import get_settings
from app.config import Settings, load_config


def setup(
        app: FastAPI,
        pool: sessionmaker
):
    db_provider = DbProvider(pool=pool)
    app.dependency_overrides[dao_provider] = db_provider.dao
    app.dependency_overrides[get_settings] = load_config
