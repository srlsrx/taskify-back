from models.user_model import User
from database.db import SessionLocal


def get_all_users():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        if not users:
            print("No hay usuarios disponibles.")
            return None
        return users
    except Exception as e:
        print(f"Error al consultar usuarios: {e}")
        return None
    finally:
        session.close()

def get_user_by_id(user_id: int):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            print(f"Usuario con ID {user_id} no existe.")
            return None
        return user
    except Exception as e:
        print(f"Error al consultar usuario: {e}")
        return None
    finally:
        session.close()

def create_user(username: str, email: str, password: str):
    session = SessionLocal()
    try:
        if not username or not email or not password:
            print("Todos los campos son obligatorios.")
            return None
        user = session.query(User).filter(User.username == username).first()
        if user:
            print(f"El usuario {username} ya existe.")
            return None
        user = User(username=username, email=email, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return None
    finally:
        session.close()

def update_user(user_id: int, username: str = None, email: str = None, password: str = None):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            print(f"Usuario con ID {user_id} no existe.")
            return None
        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.password = password
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        return None
    finally:
        session.close()

def delete_user(user_id: int):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            print(f"Usuario con ID {user_id} no existe.")
            return None
        session.delete(user)
        session.commit()
        return user
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")
        return None
    finally:
        session.close()
