from functools import wraps
from flask import abort
from flask_login import current_user

from models.User import Role

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_anonymous:
            abort(401)
        elif current_user.role != Role.ADMIN:
            abort(403)
        
        return func(*args, **kwargs)
    return decorated_view

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_anonymous:
            abort(401)
        return func(*args, **kwargs)
    return decorated_view
