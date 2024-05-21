from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase())
    ...


class User():
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str]
    is_vip: Mapped[bool]
    vip_exp_date: Mapped[str]
    permanent_vip: Mapped[bool]
    