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


def create_user(user_data):
    session = SessionLocal()
    try:
        if not user_data.username or not user_data.email or not user_data.password:
            print("Todos los campos son obligatorios.")
            return None
        user = session.query(User).filter(User.username == user_data.username).first()
        if user:
            print(f"El usuario {user_data.username} ya existe.")
            return None
        user = User(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password,
            is_admin=user_data.is_admin,
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return None
    finally:
        session.close()


def update_user(user_id: int, user_data):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            print(f"Usuario con ID {user_id} no existe.")
            return None
        if user_data.username is not None:
            user.username = user_data.username
        if user_data.email is not None:
            user.email = user_data.email
        if user_data.password is not None:
            user.password = user_data.password
        if user_data.is_admin is not None:
            user.is_admin = user_data.is_admin
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


def get_password_by_username(username: str):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if not user:
            print(f"Usuario con nombre {username} no existe.")
            return None
        return user.password
    except Exception as e:
        print(f"Error al consultar usuario: {e}")
        return None
    finally:
        session.close()


def get_user_by_username(username: str):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if not user:
            print(f"Usuario con nombre {username} no existe.")
            return None
        return user
    except Exception as e:
        print(f"Error al consultar usuario: {e}")
        return None
    finally:
        session.close()
