from dataclasses import dataclass
from .utilities.env import env


@dataclass
class Config:
    SECRET_KEY: str = env("APP_SECRET")
    SQLALCHEMY_DATABASE_URI: str = env("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
