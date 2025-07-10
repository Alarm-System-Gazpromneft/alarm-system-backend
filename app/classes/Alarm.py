

class Alarm:
    def __init__(self, id, name, description, priority, contacts_list, executor=None, cancel_list=None, finish_time=None, creation_time=None):
        self.id = id
        self.name = name
        self.description = description
        self.priority = priority
        self.contacts_list = contacts_list
        self.executor = executor #ID user
        self.cancel_list = cancel_list
        self.finish_time = finish_time
        self.creation_time = creation_time
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "priority": self.priority,
            "contacts_list": self.contacts_list,
            "executor": self.executor,
            "cancel_list": self.cancel_list,
            "finish_time": self.finish_time,
            "creation_time": self.creation_time
        }