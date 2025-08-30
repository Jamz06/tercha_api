
import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DATETIME, func, text
from sqlalchemy.orm import mapped_column, Mapped


from database.database import Base

from typing import Annotated

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
    t_chat_id: Mapped[str]



class Dog(Base):
    __tablename__ = "dog"

    id: Mapped[intpk]
    name: Mapped[name_50]
    owner: Mapped[int] = mapped_column(ForeignKey("owner.id", ondelete="CASCADE"))

# dogs_table = Table(
#     "dogs",
#     Column("id", Integer, primary_key=True),
#     Column("name", String)
# )

# class Sport(Base):
#     __table__ = "sport"

#     id: Mapped[intpk]
#     name: Mapped[name_50]

# class CardType(Base):
#     __table__ = "card_type"

#     id: Mapped[intpk]
#     name: Mapped[name_50]
#     dificulty: Mapped[int]
#     sport: Mapped[int] = mapped_column(ForeignKey("sport.id", ondelete="CASCADE"))

# class Card(Base):
#     __table__ = "card"

#     id: Mapped[intpk]
#     name: Mapped[name_50]
#     description: Mapped[str]
#     points: Mapped[int]
#     card_type: Mapped[int] = mapped_column(ForeignKey("card_type.id", ondelete="CASCADE"))

# class TaskStatus(Base):
#     __table__ = "task_status"

#     id: Mapped[intpk]
#     name: Mapped[name_50]
#     task_closed: Mapped[bool]


# class Task(Base):
#     __table__ = "task_status"

#     id: Mapped[intpk]
#     dog: Mapped[int] = mapped_column(ForeignKey("dog.id"))
#     card: Mapped[int] = mapped_column(ForeignKey("card.id"))
#     status: Mapped[int] = mapped_column(ForeignKey("status.id"))
#     who_rated: Mapped[int] = mapped_column(ForeignKey("owner.id"))
#     rate: Mapped[int]
#     start_date: Mapped[DATETIME] = mapped_column(server_default=func.now())
#     end_date: Mapped[DATETIME]
