from app.classes.Database import Database
import bcrypt
import uuid

def authorize_user_route(user):
    db = Database("khokhlovkirill.ru", "5432", "hackathon", "hackathon", "alarm_system")
    user_authorize = db.get_user_by_login(user.login)
    if user_authorize == None:
        return {
            "error": "Incorrect username or password",
        }
    if bcrypt.checkpw(user.password.encode("utf-8"), user_authorize.password_hash.encode("utf-8")):
        random_uuid = uuid.uuid4()
        db.add_uuid(user_authorize, random_uuid)
        return {
            "user": user_authorize.id,
            "uuid": random_uuid,
        }
    else:
        return {
            "error": "Incorrect username or password",
        }