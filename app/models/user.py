from typing import Optional, List
from app.models.base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.shared.address import Address


class User(Base):
    __tablename__ = 'user_account'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    username: Mapped[str] = mapped_column(String(40))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List[Address]] = relationship(
        back_populates='user_address', cascade='all, delete-orphan'
    )

    def __repr__(self) -> str:
        return f'User(id={self.id!r}, name={self.name!r})'

