from app.modules.user.user_model import User
from app.utilities.jwt import generate_password_reset_token
from app.modules.user.user_repo import update_password


def process_forgot_password(email: str) -> str | None:
    user = User.query.filter_by(email=email).first()
    if not user:
        return

    reset_token = generate_password_reset_token(user.id)
    # TODO: send email

    # TODO: dont return token, remove after testing
    return reset_token


def reset_user_password(user_id: int, new_password: str) -> None:
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return None

    return update_password(user, new_password)
