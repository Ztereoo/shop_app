from typing import TYPE_CHECKING
from .base import Base
from .mixins import UserRelationMixin
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship


class Post(UserRelationMixin, Base):
    _user_back_populates = "posts"
    title: Mapped[str]= mapped_column(String(100))
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
