from app.classes.Database import Database


def get_alarm_id_route(alarm_id):
    db = Database("khokhlovkirill.ru", "5432", "hackathon", "hackathon", "alarm_system")
    return db.get_alarm_id(alarm_id).to_dict()