from .user_model import User
from app.database.base import db
from app.utilities.password_hasher import password_hasher


def create_user(email: str, password: str) -> User:
    new_user = User()
    new_user.email=email
    new_user.password=password_hasher.hash(password)
    
    db.session.add(new_user)
    db.session.commit()
    return new_user

