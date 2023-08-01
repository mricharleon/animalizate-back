from typing import List
from app.models.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.auth.state import State


class Module(Base):
    __tablename__ = 'module'

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(40))
    description: Mapped[str] = mapped_column(String(250))

    states_module: Mapped[List['State']] = relationship(back_populates='module_state')

    def __repr__(self) -> str:
        return f'Module(id={self.id!r}, title={self.title!r})'
