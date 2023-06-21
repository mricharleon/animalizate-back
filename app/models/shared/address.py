from app.models.base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.shared.auth import Auth



class Address(Base):
    __tablename__ = 'address'
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(String(80))
    postal_code: Mapped[str] = mapped_column(String(10))

    user_id: Mapped[int] = mapped_column(ForeignKey('user_account.id'))
    user_address: Mapped['User'] = relationship(back_populates='addresses')

    auth_id: Mapped[int] = mapped_column(ForeignKey('auth.id'))
    # auth_address: Mapped['Auth'] = relationship(back_populates='addresses')

    def __repr__(self) -> str:
        return f'Address(id={self.id!r}, email_address={self.email_address!r})'
