from pydantic import BaseModel
class UserRegistration(BaseModel):
    name: str
    surname: str
    patronymic: str
    phone_number: str
    login: str
    password: str