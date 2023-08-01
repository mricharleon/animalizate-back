from typing import Optional, List
from app.models.base import Base
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.auth.module import Module


class State(Base):
    __tablename__ = 'state'

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(40))
    color: Mapped[str] = mapped_column(String(8))
    background: Mapped[str] = mapped_column(String(8))
    visible: Mapped[str] = mapped_column(Boolean())
    module: Mapped[int]

    module_id: Mapped[int] = mapped_column(ForeignKey('module.id'))
    module_state: Mapped['Module'] = relationship(back_populates='states_module')

    auth: Mapped['Auth'] = relationship(back_populates='state_auth')
