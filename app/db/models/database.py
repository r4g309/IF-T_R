from typing import Optional

from litestar.plugins.sqlalchemy import base
from sqlalchemy import CheckConstraint, String, Text
from sqlalchemy.orm import Mapped, mapped_column

# if TYPE_CHECKING:
#     from app.models.table_model import TableModel


class Database(base.UUIDAuditBase):
    __tablename__ = "database"

    name: Mapped[str] = mapped_column(String(100), index=True, unique=True)
    type: Mapped[str] = mapped_column(String(50))
    host: Mapped[str] = mapped_column(String(255))
    port: Mapped[int]
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # tables: Mapped[list["TableModel"]] = relationship(
    #     "TableModel",
    #     back_populates="database",
    #     lazy="noload",
    #     cascade="all, delete-orphan",
    # )

    __table_args__ = (
        CheckConstraint("port BETWEEN 1 AND 65535", name="chk_valid_port"),
    )
