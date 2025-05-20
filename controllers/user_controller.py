from models.task_model import Task
from models.user_model import User
from database.db import SessionLocal


def get_all_users():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return users

def get_user_by_id(user_id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user

def create_user(username: str, email: str, password: str):
    session = SessionLocal()
    user = User(username=username, email=email, password=password)
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    return user

def update_user(user_id: int, username: str = None, email: str = None, password: str = None):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    if username:
        user.username = username
    if email:
        user.email = email
    if password:
        user.password = password
    session.commit()
    session.refresh(user)
    session.close()
    return user

def delete_user(user_id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()
    return user

