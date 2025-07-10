from app.classes.Database import Database


def get_alarms_route(uuid):
    db = Database("khokhlovkirill.ru", "5432", "hackathon", "hackathon", "alarm_system")

    if not db.check_uuid(uuid):
        return {
            "error": "Unauthorized"
        }

    sp = []
    for i in db.get_all_alarms():
        sp.append(i.to_dict())
    return sp


