from typing import Optional, List
from app.models.base import Base
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship




class Module(Base):
    __tablename__ = 'module'

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(40))
    description: Mapped[str] = mapped_column(String(250))

    states_module: Mapped[List['State']] = relationship(back_populates='module_state')
