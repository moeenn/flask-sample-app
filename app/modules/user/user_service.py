from .user_model import User
from .user_repo import create_user


def register_user(email: str, password: str) -> User | None:
    exists = User.query.filter_by(email=email).first()
    if exists:
        return None

    new_user = create_user(email=email, password=password)
    return new_user
