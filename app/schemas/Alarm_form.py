from pydantic import BaseModel
class AlarmForm(BaseModel):
    name: str
    description: str
    priority: str="medium"
    contacts_list: list
