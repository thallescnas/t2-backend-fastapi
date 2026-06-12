from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean
from database import Base


class Car(Base):
    __tablename__ = "Cars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)

    modelo: Mapped[str] = mapped_column(String, nullable=False)

    ano: Mapped[int] = mapped_column(Integer, nullable=False)

    fabricante: Mapped[str] = mapped_column(String, nullable=False)

    usado: Mapped[bool] = mapped_column(String, nullable=False)


