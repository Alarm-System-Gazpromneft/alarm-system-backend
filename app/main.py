from fastapi import FastAPI
import uvicorn

from app.api.authorize_user_route import authorize_user_route
from app.api.register_user_route import register_user_route
from app.schemas.Authorization_form import UserAuthorization
from app.schemas.Registration_form import UserRegistration

from app.api.get_alarm_by_user_route import get_alarm_by_user_route
from app.api.get_alarms_route import get_alarms_route
from app.api.get_alrm_id_route import get_alarm_id_route
from app.api.get_userinfo_route import get_userinfo_route

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

#список всех проблем
@app.get("/api/get_alarms")
async def get_alarms():
    return get_alarms_route()

#информация о сотруднике по номеру телефона или ID
@app.get("/api/employees/")
async def get_empoyees(input: str, type: str):
    return get_userinfo_route(input, type)

#информация о проблеме по ее ID
@app.get("/api/alarm/{id}") #
async def get_alarm_id(id):
    return get_alarm_id_route(id)

#список проблем по ID пользователя
@app.get("/api/employees/get_alarms/{user_id}")
async def get_alarm_by_user(user_id):
    return get_alarm_by_user_route(user_id)

#регистрация пользователя
@app.post("/api/employees/register")
async def register_user(user: UserRegistration):
    return register_user_route(user)

#авторизация пользователя
@app.post("/api/employees/authorize")
async def authorize_user(user: UserAuthorization):
    return authorize_user_route(user)



uvicorn.run(app, port=8000)