from datetime import datetime, timezone
from typing import Optional
import uuid
from pydantic import BaseModel, ConfigDict
from sqlalchemy import UUID, DateTime, String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from utils.postgres import PostgresHelper


class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(String(256), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(tz=timezone.utc),
        server_default=PostgresHelper.server_timezone(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(tz=timezone.utc),
        onupdate=datetime.now(tz=timezone.utc),
        server_default=PostgresHelper.server_timezone(),
        server_onupdate=PostgresHelper.server_timezone(),
    )


class UserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    username: str
    email: Optional[str] = None
    created_at: datetime
    updated_at: datetime
