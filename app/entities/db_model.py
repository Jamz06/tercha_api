

import datetime
from sqlalchemy import (
    Boolean, Table, Column, Integer, String,
    MetaData, ForeignKey, DateTime, func, text, BigInteger, Index,
    Identity
)
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.sql import expression

from database.database import Base

from typing import Annotated, Optional

# из документаци алхимии, удобно переиспользовать типы в классах таблиц, если объявить заранее
# первичный ключ
intpk = Annotated[int, mapped_column(primary_key=True)]
name_50 = Annotated[str, 50]

created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    )]

metadata_obj = MetaData()

class Owner(Base):
    __tablename__ = "owner"

    id: Mapped[intpk]
    username: Mapped[name_50]
    # chatid для телеграм
    t_chat_id: Mapped[int] = mapped_column(
        BigInteger
    )

    dogs: Mapped[list["Dog"]] = relationship(
        back_populates="owner"
    )

    # создать индекс по chat_id
    __table_args__ = (
        Index("chatid_idx","t_chat_id"),
    )


class Dog(Base):
    __tablename__ = "dog"

    id: Mapped[intpk]
    name: Mapped[name_50]
    owner_id: Mapped[int] = mapped_column(ForeignKey("owner.id", ondelete="CASCADE"))
    owner: Mapped["Owner"] = relationship(
        back_populates="dogs"
    )
    tasks: Mapped[list["Task"]] = relationship(
        back_populates="dog_task"
    )



class Sport(Base):
    __tablename__ = "sport"

    id: Mapped[intpk]
    name: Mapped[name_50]

class CardType(Base):
    __tablename__ = "card_type"

    id: Mapped[intpk]
    name: Mapped[name_50]
    dificulty: Mapped[int]
    sport: Mapped[int] = mapped_column(ForeignKey("sport.id", ondelete="CASCADE"))
    
    # Список всех доступных карточек с заданиями по типу карточки
    cards_avail: Mapped["Card"] = relationship(
        back_populates="card_type"
    )

class Card(Base):
    __tablename__ = "card"

    id: Mapped[intpk]
    name: Mapped[name_50]
    description: Mapped[str]
    points: Mapped[int]
    card_type_id: Mapped[int] = mapped_column(ForeignKey("card_type.id", ondelete="CASCADE"))
    # Доступность карточки
    available: Mapped[bool] = mapped_column(
        Boolean, default=True,
        server_default=expression.false(), nullable=False
    )

    card_type: Mapped["CardType"] = relationship(
        back_populates="cards_avail"
    )

class TaskStatus(Base):
    __tablename__ = "task_status"

    id: Mapped[intpk]
    name: Mapped[name_50]
    task_closed: Mapped[bool]


class Task(Base):
    __tablename__ = "status"

    id: Mapped[intpk]
    dog: Mapped[int] = mapped_column(ForeignKey("dog.id"))
    card: Mapped[int] = mapped_column(ForeignKey("card.id"))
    status: Mapped[int] = mapped_column(ForeignKey("task_status.id"))
    who_rated: Mapped[Optional[int]] = mapped_column(ForeignKey("owner.id"))
    rate: Mapped[Optional[int]]
    start_date: Mapped[created_at]
    end_time: Mapped[Optional[datetime.datetime]]

    dog_task: Mapped[list["Dog"]] = relationship(
        back_populates="tasks"
    )