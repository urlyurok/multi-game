import os

# Получаем URL подключения к базе данных из переменной окружения

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:Xx123321@localhost:5432/game_base")
