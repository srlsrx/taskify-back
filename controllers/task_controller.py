from models.task_model import Task
from models.user_model import User
from database.db import SessionLocal
from sqlalchemy.orm import joinedload

def create_task(name: str, description: str, user_id: int):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if not name:
            print("El nombre es obligatorio.")
            return None
        if not user:
            print(f"Usuario con ID {user_id} no existe.")
            return None
        task = Task(name=name, description=description, user_id=user_id)
        session.add(task)
        session.commit()
        session.refresh(task)
        task = session.query(Task).options(joinedload(Task.user)).filter(Task.id == task.id).first()
        return task
    except Exception as e:
        print(f"Error al crear tarea: {e}")
        return None
    finally:
        session.close()


def get_all_tasks():
    session = SessionLocal()
    try:
        tasks = session.query(Task).options(joinedload(Task.user)).all()
        return tasks
    except Exception as e:
        print(f"Error al obtener tareas: {e}")
        return None
    finally:
        session.close()

def get_task_by_id(task_id: int):
    session = SessionLocal()
    try:
        task = session.query(Task).options(joinedload(Task.user)).filter(Task.id == task_id).first()
        if not task:
            print(f"Tarea con ID {task_id} no existe.")
            return None
        return task
    except Exception as e:
        print(f"Error al consultar tarea: {e}")
        return None
    finally:
        session.close()


def update_task(task_id: int, name: str = None, description: str = None, is_done: bool = None):
    session = SessionLocal()
    try:
        task = session.query(Task).options(joinedload(Task.user)).filter(Task.id == task_id).first()
        if not task:
            print(f"Tarea con ID {task_id} no existe.")
            return None
        if name:
            task.name = name
        if description:
            task.description = description
        if is_done is not None:
            task.is_done = is_done
        session.commit()
        session.refresh(task)
        return task
    except Exception as e:
        print(f"Error al actualizar tarea: {e}")
        return None
    finally:
        session.close()


def delete_task(task_id: int):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            print(f"Tarea con ID {task_id} no existe.")
            return None
        session.delete(task)
        session.commit()
        return task
    except Exception as e:
        print(f"Error al consultar tarea: {e}")
        return None
    finally:
        session.close()


def get_tasks_by_user(user_id: int):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            print(f"Usuario con ID {user_id} no existe.")
            return None
    except Exception as e:
        print(f"Error al consultar usuario: {e}")
        return None
    tasks = session.query(Task).filter(Task.user_id == user_id).all()
    session.close()
    return tasks
