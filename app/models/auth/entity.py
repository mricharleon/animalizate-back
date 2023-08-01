from app.models.base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.auth.state import State


class Entity(Base):
    __tablename__ = 'entity'

    id: Mapped[int] = mapped_column(primary_key=True)

    # company data
    access: Mapped[str] = mapped_column(String(40))
    business_name: Mapped[str] = mapped_column(String(125))
    business_id: Mapped[str] = mapped_column(String(15))

    # One To One
    state_id: Mapped[int] = mapped_column(ForeignKey('state.id'))
    state_auth: Mapped['State'] = relationship(back_populates='auth')

    # connection details to the database
    ip_db: Mapped[str] = mapped_column(String(40))
    port_db: Mapped[str] = mapped_column(String(8))
    name_db: Mapped[str] = mapped_column(String(40))
    user_db: Mapped[str] = mapped_column(String(30))
    pass_db: Mapped[str] = mapped_column(String(50))
    scheme_db: Mapped[str] = mapped_column(String(50))

    # other data
    logo: Mapped[str] = mapped_column(String(200))
    theme: Mapped[str] = mapped_column(String(40))

    def __repr__(self) -> str:
        return f'Entity(id={self.id!r}, access={self.access!r})'

