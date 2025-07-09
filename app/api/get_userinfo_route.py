from app.classes.User import User
from app.classes.Database import Database


def get_userinfo_route(input_str: str, type: str):
    db = Database("khokhlovkirill.ru", "5432", "hackathon", "hackathon", "alarm_system")
    if type == 'phone':
        return db.get_user_by_phone(input_str).to_dict()
    else:
        return db.get_user_by_id(input_str).to_dict()