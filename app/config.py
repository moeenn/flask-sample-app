from dataclasses import dataclass
from .utilities.env import env


@dataclass
class Config:
    app_secret: str = env("APP_SECRET")
    database_uri: str = env("DATABASE_URI")
