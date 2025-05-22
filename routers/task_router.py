

from fastapi import APIRouter, HTTPException
from controllers.task_controller import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
    get_tasks_by_user
)
from schemas.task_schemas import TaskCreate, TaskOut, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskOut])
def list_tasks():
    tasks = get_all_tasks()
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found")
    return tasks

@router.get("/{task_id}", response_model=TaskOut)
def read_task(task_id: int):
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=TaskOut, status_code=201)
def create_new_task(task: TaskCreate):
    new_task = create_task(task.name, task.description, task.user_id)
    if not new_task:
        raise HTTPException(status_code=400, detail="Task creation failed")
    return new_task

@router.put("/{task_id}", response_model=TaskOut)
def update_existing_task(task_id: int, task: TaskUpdate):
    updated_task = update_task(task_id, task.name, task.description, task.is_done)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/{task_id}", status_code=204)
def delete_existing_task(task_id: int):
    deleted = delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")

@router.get("/user/{user_id}", response_model=list[TaskOut])
def list_tasks_by_user(user_id: int):
    tasks = get_tasks_by_user(user_id)
    if tasks is None or len(tasks) == 0:
        raise HTTPException(status_code=404, detail="No tasks found for this user")
    return tasks
