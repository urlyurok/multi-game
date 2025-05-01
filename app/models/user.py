from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import validates, relationship
from datetime import datetime, timezone
from app.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    games_played = Column(Integer, default=0)
    total_clicks = Column(Integer, default=0)
    successful_clicks = Column(Integer, default=0)
    failed_clicks = Column(Integer, default=0)
    most_used_color = Column(String)

    # Связи с другими таблицами
    # Игры, в которых участвует пользователь
    games = relationship('Game', back_populates='winner')
    # Все клики пользователя
    clicks = relationship('Click', back_populates='user')
    game_statistics = relationship(
        'GameStatistics', back_populates='user')  # Статистика по играм

    @validates("email")
    def validate_email(self, key, email):
        if "@" not in email:
            raise ValueError("Email должен содержать '@'")
        return email
