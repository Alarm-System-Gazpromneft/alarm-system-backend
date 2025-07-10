from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

app.add_middleware(
  CORSMiddleware,
  allow_origins = ["*"],
  allow_methods = ["*"],
  allow_headers = ["*"]
)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

#список всех проблем
@app.get("/api/get_alarms")
async def get_alarms(uuid=None):
    return get_alarms_route(uuid)

#информация о сотруднике по номеру телефона или ID
@app.get("/api/employees/")
async def get_empoyees(input: str, type: str, uuid=None):
    return get_userinfo_route(uuid, input, type)

#информация о проблеме по ее ID
@app.get("/api/alarm/{id}") #
async def get_alarm_id(id, uuid=None):
    return get_alarm_id_route(uuid, id)

#список проблем по ID пользователя
@app.get("/api/employees/get_alarms/{user_id}")
async def get_alarm_by_user(user_id, uuid=None):
    return get_alarm_by_user_route(uuid, user_id)

#регистрация пользователя
@app.post("/api/employees/register")
async def register_user(user: UserRegistration):
    return register_user_route(user)

#авторизация пользователя
@app.post("/api/employees/authorize")
async def authorize_user(user: UserAuthorization):
    return authorize_user_route(user)



#uvicorn.run(app, host='0.0.0.0', port=8000)