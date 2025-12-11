from __future__ import annotations

from typing import TYPE_CHECKING

from app.domain.dictionary.services import DatabaseService

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncSession


async def provide_databases_service(
    db_session: AsyncSession | None = None,
) -> AsyncGenerator[DatabaseService, None]:
    async with DatabaseService.new(
        session=db_session,
        error_messages={
            "duplicate_key": "Current database already exists",
            "foreign_key": "Database is used by other entities",
            "integrity": "Database integrity error",
        },
    ) as service:
        yield service
