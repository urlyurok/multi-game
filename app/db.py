from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Импортируем строку подключения из конфигурации
from app.config import DATABASE_URL

# Создаем движок подключения к базе данных
engine = create_engine(DATABASE_URL)

# Создаем класс SessionLocal для создания сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для всех моделей
Base = declarative_base()

# Функция для получения сессии (используется как зависимость в FastAPI)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Функция для инициализации базы данных (создание таблиц)


def init_db():
    Base.metadata.create_all(bind=engine)
