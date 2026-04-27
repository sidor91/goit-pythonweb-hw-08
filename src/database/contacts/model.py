from datetime import datetime, date

from sqlalchemy import Integer, String, Date, Index, func
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.sql.sqltypes import DateTime


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"

    __table_args__ = (Index("ix_contacts_full_name", "first_name", "second_name"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    second_name: Mapped[str | None] = mapped_column(String(50), nullable=True, unique=False)
    email: Mapped[str | None] = mapped_column(String(50), nullable=True, unique=True)
    birthday: Mapped[date | None] = mapped_column(Date, nullable=True, unique=False)
    additional_info: Mapped[str | None] = mapped_column(
        String(250), nullable=True, unique=False
    )
    created_at: Mapped[datetime] = mapped_column(
        "created_at", DateTime, default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        "updated_at", DateTime, default=func.now(), onupdate=func.now()
    )
