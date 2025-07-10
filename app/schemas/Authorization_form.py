from pydantic import BaseModel
class UserAuthorization(BaseModel):
    login: str
    password: str