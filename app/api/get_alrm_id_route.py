from app.classes.Database import Database


def get_alarm_id_route(uuid, alarm_id):
    db = Database("khokhlovkirill.ru", "5432", "hackathon", "hackathon", "alarm_system")
    if not db.check_uuid(uuid):
        return {
            "error": "Unauthorized"
        }
    return db.get_alarm_id(alarm_id).to_dict()