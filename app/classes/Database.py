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
            spisok.append(Alarm(alarm[0], alarm[1], alarm[2], alarm[3], alarm[4], alarm[5], alarm[6], alarm[7], alarm[8]))
        return spisok

    def get_all_users(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        spisok = []
        for user in cursor.fetchall():
            spisok.append(User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8]))
        return spisok

    def get_user_by_id(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", user_id)
        return User(*cursor.fetchone())

    def get_user_by_phone(self, phone_number):
        cursor = self.conn.cursor()
        print(phone_number)
        cursor.execute(f"SELECT * FROM users WHERE phone_number = '+{phone_number}'")
        return User(*cursor.fetchone())


db = Database("khokhlovkirill.ru", "5432", "hackathon", "hackathon", "alarm_system")
print(db.get_all_alarms()[1].name)

