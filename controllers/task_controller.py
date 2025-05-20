# - ✅ Crear una tarea con título y descripción
# - ✅ Ver todas las tareas existentes
# - ✅ Consultar una tarea por ID
# - ✅ Actualizar una tarea existente (título, descripción o estado)
# - ✅ Eliminar una tarea

from models.task_model import Task
from models.user_model import User
from database.db import SessionLocal

def create_task(name: str, description: str, user_id: int):
    session = SessionLocal()
    task = Task(name=name, description=description, user_id=user_id)
    session.add(task)
    session.commit()
    session.refresh(task)
    session.close()
    return task


def get_all_tasks():
    session = SessionLocal()
    session.close()
    return session.query(Task).all()

def get_task_by_id(task_id: int):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    session.close()
    return task


def update_task(task_id: int, name: str = None, description: str = None, is_done: bool = None):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    if name:
        task.name = name
    if description:
        task.description = description
    if is_done is not None:
        task.is_done = is_done
    session.commit()
    session.refresh(task)
    session.close()
    return task


def delete_task(task_id: int):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
        session.close()
        return task


def get_tasks_by_user(user_id: int):
    session = SessionLocal()
    tasks = session.query(Task).filter(Task.user_id == user_id).all()
    session.close()
    return tasks