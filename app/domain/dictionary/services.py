from advanced_alchemy.service import (
    SQLAlchemyAsyncRepositoryService,
)

from app.db.models.database import Database
from app.domain.dictionary.repositories import DatabaseRepository


class DatabaseService(SQLAlchemyAsyncRepositoryService[Database]):
    repository_type = DatabaseRepository
