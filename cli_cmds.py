from flask.cli import AppGroup

from app import db, bcrypt
from models.User import User
from seed import users

seed_cli = AppGroup("seed")

@seed_cli.command("users")
def seed_movies():
    for user in users:
        user['password'] = bcrypt.generate_password_hash(user.get('password')) # encrypt password
        db.session.add(User(**user))
    db.session.commit()

