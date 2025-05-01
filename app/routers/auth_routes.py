from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user import User
from app.auth.auth import verify_password, create_access_token, get_password_hash

router = APIRouter()

# Регистрация нового пользователя


@router.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    # Проверка, существует ли пользователь с таким логином
    db_user = db.query(User).filter(User.username == username).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Пользователь уже существует"
        )

    # Хешируем пароль
    hashed_password = get_password_hash(password)

    # Создаём нового пользователя
    new_user = User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Пользователь зарегистрирован"}

# Логин и получение токена


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if user is None or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверный логин или пароль"
        )

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
