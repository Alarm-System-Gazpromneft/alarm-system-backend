from fastapi import FastAPI
import uvicorn

from app.api.get_alarms_route import get_alarms_route
from app.api.get_userinfo_route import get_userinfo_route

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/api/get_alarms")
async def get_alarms():
    return get_alarms_route()

@app.get("/api/employees/")
async def get_empoyees(input: str, type: str):
    return get_userinfo_route(input, type)


uvicorn.run(app, host="0.0.0.0", port=8000)