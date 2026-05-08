from src.database.config import Base
from pydantic import ConfigDict

class User(Base):
    id: int
    username: str
    email: str
    avatar: str

    model_config = ConfigDict(from_attributes=True)


class UserCreate(Base):
    username: str
    email: str
    password: str


class Token(Base):
    access_token: str
    token_type: str
