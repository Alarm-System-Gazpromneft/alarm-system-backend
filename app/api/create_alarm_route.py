from app.classes.CallModule import CallModule
from app.classes.Database import Database


def prioritize_contacts(spisok_contacts):
    return spisok_contacts
def create_alarm_route(alarm):
    db = Database("khokhlovkirill.ru", "5432", "hackathon", "hackathon", "alarm_system")
    alarm_id = db.get_max_id().id + 1
    db.create_alarm(alarm, alarm_id)
    call_contacts(alarm.contacts_list, alarm, db, alarm_id)
    return {
        "id": alarm_id,
        "name": alarm.name,
        "description": alarm.description,
        "contacts_list": alarm.contacts_list,
    }

def call_contacts(spisok_contacts, alarm, db, alarm_id):
    spisok_contacts_sorted = prioritize_contacts(spisok_contacts)
    for contact in spisok_contacts_sorted:
        object_call = CallModule(host="10.82.210.62", port=8765)
        if not object_call.call(contact):
            continue
        object_call.speak(f"Здравствуйте! Возникла проблема. {alarm.name} Введите, пожалуйста, пин-код.")
        for i in range(3):
            if object_call.dtmf_received(db.get_user_by_phone(contact).pin_code):
                object_call.speak(f"Прослушайте описание проблемы. {alarm.description}. Если вы готовы взять в работу данную проблему, нажмите один или скажите принять, иначе, нажмите ноль или скажите отклонить.")
                if object_call.work_with_problem():
                    db.do_executor(contact, alarm_id)
                object_call.hangup()
                break
            elif i == 2:
                object_call.hangup()
            object_call.speak(f"Неверный код. Введите его повторно.")





