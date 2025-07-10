from app.classes.Database import Database
import bcrypt
from random import randint


def register_user_route(user):
    password_hash = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    a = randint(0, 999999)
    pin_code = (6 - len(str(a))) * '0' + str(a)
    db = Database("khokhlovkirill.ru", "5432", "hackathon", "hackathon", "alarm_system")
    return db.register_user(user.name, user.surname, user.patronymic, user.phone_number, user.login, password_hash, pin_code)
