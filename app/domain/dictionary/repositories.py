from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from app.db.models.database import Database


class DatabaseRepository(SQLAlchemyAsyncRepository[Database]):
    model_type = Database
