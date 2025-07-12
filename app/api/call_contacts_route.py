from app.classes.Database import Database
import websocket

def call_contacts_route(contact, problem):

    return




def create_alarm_route(alarm):
    db = Database("khokhlovkirill.ru", "5432", "hackathon", "hackathon", "alarm_system")
    db.create_alarm(alarm)
    return {
        "name": alarm.name,
        "description": alarm.description,
        "contacts_list": alarm.contacts_list,
    }