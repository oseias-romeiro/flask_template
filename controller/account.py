from datetime import datetime

from models.User import User
from app import db, bcrypt

def getUserByUsername(username: str) -> User:
    return db.session.query(User).filter_by(
        username=username
    ).first()

def verifyPassword(hash: str, password: str) -> bool:
    return bcrypt.check_password_hash(hash, password)

def updateLastLogin(user: User)  -> User:
    user.lastLogin = datetime.now()
    db.session.commit()
    return user

def createUser(username, email, password) -> User:
    user = User(
        username=username,
        email=email,
        password=bcrypt.generate_password_hash(password)
    )
    db.session.add(user)
    db.session.commit()
    return user

def deleteUser(username: str) -> User:
    user = getUserByUsername(username)
    db.session.delete(user)
    db.session.commit()
    return user

def getUsersAll(limit=10, offset=0) -> list[User]:
    return db.session.query(User).limit(limit).offset(offset).all()

def editUser(id, username, email, password) -> User:
    user = getUserById(id)
    if verifyPassword(user.password, password):
        user.username = username
        user.email = email
        user.updateAt = datetime.now()
        db.session.commit()
    else:
        raise Exception("Password incorrect")

    return user

def changePassword(id, password) -> User:
    user = getUserById(id)
    user.password = bcrypt.generate_password_hash(password)
    user.updateAt = datetime.now()

    db.session.commit()

    return user

def getUserByEmail(email: str) -> User:
    return db.session.query(User).filter_by(
        email=email
    ).first()

def getUserById(id: int) -> User:
    return db.session.query(User).get(id)

def changeRole(username: str, role: int) -> User:
    user = getUserByUsername(username)
    user.role = role
    db.session.commit()
    return user
