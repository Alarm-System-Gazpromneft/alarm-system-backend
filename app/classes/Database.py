import datetime
import json
import psycopg2
from app.classes.Alarm import Alarm
from app.classes.User import User

class Database:
    def __init__(self, host, port, user, password, dbname):
        # Подключение к базе данных postgres
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
    def get_all_alarms(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM alarm")
        spisok = []
        for alarm in cursor.fetchall():
            spisok.append(Alarm(*alarm))
        return spisok

    def get_all_users(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        spisok = []
        for user in cursor.fetchall():
            spisok.append(User(*user))
        return spisok

    def get_user_by_id(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", user_id)
        return User(*cursor.fetchone())

    def get_user_by_phone(self, phone_number):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE phone_number = '+{phone_number}'")
        return User(*cursor.fetchone())

    def get_user_by_login(self, login):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE login = '{login}'")
        a = cursor.fetchone()
        if a != None:
            return User(*a)
        else:
            return None

    def get_max_id(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM alarm ORDER BY id ASC LIMIT 1")
        return Alarm(*cursor.fetchone())

    def do_executor(self, phone_number, id_alarm):
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE alarm SET executor='{self.get_user_by_phone(phone_number).id}' WHERE id = '{id_alarm}'")
        self.conn.commit()

    def get_alarm_id(self, alarm_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM alarm WHERE id = %s", alarm_id)
        return Alarm(*cursor.fetchone())

    def get_alarm_by_user(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM alarm WHERE executor = %s", user_id)
        spisok_alarms = []
        for alarm in cursor.fetchall():
            spisok_alarms.append(Alarm(*alarm))
        return spisok_alarms

    def register_user(self, name, surname, patronymic, phone_number, login, password_hash, pin_code):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (name, surname, patronymic, phone_number, login, password_hash, pin_code) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, surname, patronymic, phone_number, login, password_hash, pin_code))
        self.conn.commit()

    def add_uuid(self, user, uuid):
        expiry_time = datetime.datetime.now().timestamp() + 86400
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO users_uuid ("user", uuid, expiry_time) VALUES (%s, %s, to_timestamp(%s))', (user.id, str(uuid), expiry_time))
        self.conn.commit()

    def check_uuid(self, uuid):
        if uuid is None: return False
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM users_uuid WHERE uuid = '{uuid}'")
        a = cursor.fetchone()
        if (a is not None) and a[4].timestamp() > datetime.datetime.now().timestamp():
            return True
        else:
            return False

    def create_alarm(self, alarm, id_alarm):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO alarm (id, name, description, priority, contacts_list) VALUES (%s, %s, %s, %s, %s)',
                       (id_alarm, alarm.name, alarm.description, alarm.priority, json.dumps(alarm.contacts_list)))
        self.conn.commit()