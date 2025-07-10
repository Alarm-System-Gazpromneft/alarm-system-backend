class User:
    def __init__(self, id: int, name: str, surname: str, patronymic: str, phone_number, register_datetime, activity_datetime, login: str, password_hash: str, pin_code: str):
        self.id = id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone_number = phone_number
        self.register_datetime = register_datetime
        self.activity_datetime = activity_datetime
        self.login = login
        self.password_hash = password_hash
        self.pin_code = pin_code
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "patronymic": self.patronymic,
            "phone_number": self.phone_number,
            "register_datetime": self.register_datetime,
            "activity_datetime": self.activity_datetime,
            "login": self.login,
            "password_hash": self.password_hash,
            "pin_code": self.pin_code,
        }