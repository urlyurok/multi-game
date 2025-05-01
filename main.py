from fastapi import FastAPI
from app.routers.auth_routes import router as auth_router
from app.routers.game import router as game_router
from app.routers.user_routes import router as user_router


app = FastAPI()

# Регистрация маршрутов

app.include_router(auth_router)
app.include_router(game_router)
app.include_router(user_router)

# Основная страница


@app.get("/")
def read_root():
    return {"message": "Привет в игре Smehkub"}
