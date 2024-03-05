from functools import wraps
from flask import abort
from flask_login import current_user

from models.User import Role

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != Role.ADMIN:
            abort(403)
        return func(*args, **kwargs)
    return decorated_view
