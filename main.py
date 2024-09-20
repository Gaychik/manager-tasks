from fastapi import FastAPI
from users.api import *
from tasks.api import *

app=FastAPI()

# Включаем маршруты пользователей
app.include_router(router_u, prefix="/users", tags=["users"])

# Включаем маршруты задач
app.include_router(router_t, prefix="/tasks", tags=["tasks"])




#