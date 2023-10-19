import jwt
from app.config import Config
from datetime import datetime, timedelta, timezone


def generate_password_reset_token(user_id: int) -> str:
    # auto expire token after n minutes
    expiry = datetime.now(tz=timezone.utc) + timedelta(minutes=30)

    return jwt.encode(
        {"user_id": user_id, "scope": "forgot_password", "exp": expiry},
        Config.SECRET_KEY,
        algorithm="HS256",
    )


def validate_password_reset_token(token: str) -> int | None:
    try:
        payload = jwt.decode(token, key=Config.SECRET_KEY, algorithms=["HS256"])
    except Exception:
        return None

    if not payload or not payload["user_id"] or not payload["scope"]:
        return None

    if payload["scope"] != "forgot_password":
        return None

    return payload["user_id"]
