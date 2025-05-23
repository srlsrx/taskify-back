# 📝 Proyecto TODO List - Python Vanilla + PostgreSQL

This repository contains the **backend** of a console-based To-Do List application built with **Python**, **PostgreSQL**, and the **MVC architecture pattern**, using **SQLAlchemy** and **Alembic** for ORM and migrations. It was later extended to support a REST API to connect with a React frontend.

> 🔐 The application includes a login system with role-based access. Admin users can manage both tasks and users. Regular users can manage only their tasks.

## 🖼️ Console App

![Console Screenshot 1](./src/public/console1.png)
![Console Screenshot 2](./src/public/console2.png)
![Console Screenshot 3](./src/public/console3.png)

---

## 💡 Key Concepts

-   Virtual environments and professional project structure
-   PostgreSQL integration with Python using pg8000
-   ORM with SQLAlchemy
-   Alembic for migration handling
-   MVC (Model-View-Controller) pattern
-   Console UI with `input()` and `print()`
-   User authentication and role-based access
-   REST API endpoints

---

## ✅ Features

### 🔐 Authentication

-   Login with username and password
-   Admin or regular user roles

### 📋 Tasks

-   Create a task (title + description)
-   View all tasks
-   View task by ID
-   Update task (title, description, status)
-   Delete task

### 👥 Users (Admin only)

-   View users
-   Add new users
-   Delete users

---

## 🔧 Technical Stack

-   Python 3.11+
-   PostgreSQL
-   SQLAlchemy
-   Alembic
-   pg8000
-   MVC Architecture

---

## 📁 Project Structure

todo_list/
├── models/ # SQLAlchemy models
├── controllers/ # Business logic
├── database/ # Database connection
├── views/ # Console interface
├── alembic/ # Database migrations
├── requirements.txt # Dependencies
├── README.md # Documentation
└── ENUNCIADO.md # Original assignment

## ⚙️ Installation

1. Clone the repository
   `git clone https://github.com/your-username/backend-todo-list.git`
   `cd backend-todo-list`
2. Create and activate a virtual environment
   `python3 -m venv venv`
   `source venv/bin/activate` # or `venv\Scripts\activate` on Windows
3. Install dependencies
   `pip install -r requirements.txt`
4. Configure your PostgreSQL database connection in .env or database/config.py
   Run Alembic migrations
5. Launch the app
   `python3 -m views.start_menu`

📌 Bonus Features
Input validation
Styled and friendly console menu
Colorful feedback messages
Anything extra the team decided to implement 😉

📜 License
MIT License

## ⚙️ Configuración inicial

### 1. Clona el repositorio (si es necesario)

```bash
git clone <url-del-repo>
cd todo_list
```

### 2. Crea y activa entorno virtual

```bash
python -m venv venv
.env\Scriptsctivate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

---

## 🛠️ Base de datos

### 1. Crea la base de datos en PostgreSQL

Usa este comando (fuera del entorno virtual):

```bash
psql -U postgres -c "CREATE DATABASE todo_db;"
```

> Asegúrate de tener acceso a `psql` y que tu contraseña sea `1234`.  
> Puedes modificarla en `database/db.py`.

---

## 🔗 Conexión a PostgreSQL

Edita `database/db.py` y asegúrate de que esta línea esté así:

```python
DATABASE_URL = "postgresql+pg8000://postgres:1234@localhost/todo_db"
```

> Usamos el driver `pg8000` en lugar de `psycopg2`.

---

## 🔄 Migraciones

### 1. Inicializa Alembic (si no está hecho)

```bash
alembic init alembic
```

### 2. Configura Alembic

-   En `alembic.ini` revisa:

    ```ini
    sqlalchemy.url = postgresql+pg8000://postgres:1234@localhost/todo_db
    ```

-   En `alembic/env.py`, importa el modelo y apunta a los metadatos:

    ```python
    from database.db import Base
    from models.task_model import Task
    target_metadata = Base.metadata
    ```

### 3. Crea y aplica la migración

```bash
alembic revision --autogenerate -m "crear tabla tasks y users"
alembic upgrade head
```

---

## 🚀 Ejecutar la aplicación

Lanza el menú desde la raíz del proyecto:

```bash
python views/start_menu.py
```

Y verás:

```
--- MENÚ TO-DO LIST ---
1. Crear tarea
2. Ver todas las tareas
3. Ver tarea por ID
4. Actualizar tarea
5. Eliminar tarea
6. Salir
```

---

## 🧠 Estructura del proyecto

```
todo_list/
│
├── alembic/              # Archivos de migración
├── controllers/          # Lógica de negocio (CRUD)
├── database/             # Conexión a la DB
├── models/               # Definición de modelos SQLAlchemy
├── views/                # Interfaz por consola
│
├── alembic.ini
├── requirements.txt
├── README.md
```

---

## 🧹 Notas finales

-   No necesitas frontend, puedes ver la salida por consola.
-   El objetivo es entender cómo se estructura un proyecto con MVC y SQLAlchemy.

¡Disfruta programando! 🐍✨
