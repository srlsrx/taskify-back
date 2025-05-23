from fastapi import APIRouter, HTTPException
from schemas.user_schemas import UserCreate, UserOut, UserUpdate
from controllers.user_controller import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
    get_user_by_username,
    get_user_by_email
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserOut])
def list_users():
    return get_all_users()

@router.get("/id/{user_id}", response_model=UserOut)
def read_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserOut, status_code=201)
def create_new_user(user: UserCreate):
    existing_user = get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    existing_email = get_user_by_email(user.email)
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    created_user = create_user(user)
    if not created_user:
        raise HTTPException(status_code=400, detail="Can´t create the user")
    return created_user

@router.put("/{user_id}", response_model=UserOut)
def update_existing_user(user_id: int, user: UserUpdate):
    updated_user = update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", status_code=204)
def delete_existing_user(user_id: int):
    deleted = delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")

@router.get("/user/{user_username}", response_model=UserOut)
def read_user_by_username(user_username: str):
    user = get_user_by_username(user_username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
