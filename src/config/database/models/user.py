from src.config.database.models.base.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BIGINT


class User(Base):
    __tablename__ = "users"

    id: Mapped[BIGINT] = mapped_column(primary_key=True)
    guild_id: Mapped[BIGINT]