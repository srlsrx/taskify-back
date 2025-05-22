from fastapi import FastAPI
from routers.user_router import router as user_router
from routers.task_router import router as task_router

app = FastAPI()

app.include_router(user_router)
app.include_router(task_router)
