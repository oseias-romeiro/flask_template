from models.User import User
from app import login_manager, db

@login_manager.user_loader
def load_user(uid):
    if not uid or uid == "None":
        return None
    return User.query.get(int(uid))
