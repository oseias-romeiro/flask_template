from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from sqlalchemy import Integer, String
from flask_login import UserMixin

from app import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(80), nullable=False, unique=True)
    email = mapped_column(String(80), nullable=False, unique=True)
    password = mapped_column(String(80), nullable=False)

    def __repr__(self):
        return f"user ({self.id}, {self.username})"
