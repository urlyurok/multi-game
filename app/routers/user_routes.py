from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user_by_email

router = APIRouter()

# Зависимость для получения сессии


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Регистрация пользователя


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Электронная почта уже зарегистрирована"
        )
    return create_user(db=db, username=user.username, email=user.email, password=user.password)


@router.get("/users")
def get_users():
    return {"users": ["user1", "user2", "user3"]}
