from app.modules.user.user_repo import User


def process_forgot_password(email: str) -> None:
    user = User.query.filter_by(email=email).first()
    if not user:
        return
    
    # implement auto-expiring scoped JWT