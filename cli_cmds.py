from flask.cli import AppGroup
import json

from app import db, bcrypt
from models.User import User


users = json.load(open("seeds/users.json"))

seed_cli = AppGroup("seed")

@seed_cli.command("users")
def seed_movies():
    for user in users:
        user['password'] = bcrypt.generate_password_hash(user.get('password')) # encrypt password
        db.session.add(User(**user))
    
    db.session.commit()

