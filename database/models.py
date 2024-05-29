from sqlalchemy import Boolean, Date, DateTime, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase())
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class User(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(25), nullable=False)
    is_vip: Mapped[bool] = mapped_column(Boolean)
    vip_exp_date: Mapped[str] = mapped_column(Date)
    permanent_vip: Mapped[bool] = mapped_column(Boolean)