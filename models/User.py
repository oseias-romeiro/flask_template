from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin

Base = declarative_base()


class User(UserMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)

    def __repr__(self):
        return "username: %r" % self.username
