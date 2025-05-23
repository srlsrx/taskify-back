from fastapi import FastAPI
from routers.user_router import router as user_router
from routers.task_router import router as task_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Taskify API",
    description="API de gestión de tareas y usuarios para la app Taskify",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(task_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
