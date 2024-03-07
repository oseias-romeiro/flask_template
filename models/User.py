from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, DateTime, Enum
from flask_login import UserMixin
from datetime import datetime
from app import db
import enum

class Role(enum.Enum):
    ADMIN = 1
    USER = 0

    def __str__(self) -> str: return self.name

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(30), nullable=False, unique=True)
    email = mapped_column(String(80), nullable=False, unique=True)
    password = mapped_column(String(255), nullable=False)
    role = mapped_column(Enum(Role), default=Role.USER)
    createAt = mapped_column(DateTime, default=datetime.now())
    updateAt = mapped_column(DateTime, default=datetime.now())
    lastLogin = mapped_column(DateTime, default=datetime.now())

    def __repr__(self): return f"user ({self.id}, {self.username})"
