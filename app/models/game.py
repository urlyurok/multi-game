from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(DateTime, default=datetime.now(
        timezone.utc))  # Используем UTC-время
    end_time = Column(DateTime, nullable=True)
    winner_id = Column(Integer, ForeignKey('users.id'))
    # Состояние игры, например, "in_progress", "completed"
    status = Column(String, default="in_progress")

    # Отношение к пользователю, который выиграл игру
    winner = relationship('User', back_populates='games')
