from app.classes.Database import Database


def get_alarms_route():
    db = Database("khokhlovkirill.ru", "5432", "hackathon", "hackathon", "alarm_system")

    sp = []
    for i in db.get_all_alarms():
        sp.append(i.to_dict())
    return sp


