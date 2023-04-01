# Все классы и функции для асинхронной работы
# находятся в модуле sqlalchemy.ext.asyncio.
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:
    @declared_attr
    def __tablename__(cls):

Base = declarative_base()

engine = create_async_engine(settings.database_url)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
