from typing import Optional, Union

from fastapi import Depends, Request
from fastapi_users import (BaseUserManager,
                           FastAPIUsers,
                           IntegerIDMixin,
                           InvalidPasswordException)
from fastapi_users.authentication import (AuthenticationBackend,
                                          BearerTransport,
                                          JWTStrategy)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.db import get_async_session
from app.models.user import User
from app.schemas.user import UserCreate


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

bearer_transport = BearerTransport(tokenUrl='auth/jwt/login')

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.secret, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(name='jwt',  # Произвольное имя бэкенда (должно быть уникальным).
                                     transport=bearer_transport,
                                     get_strategy=get_jwt_strategy,)
