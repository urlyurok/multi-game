from sqlalchemy import Column, Integer, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship
from app.db import Base


class GameStatistics(Base):
    __tablename__ = 'game_statistics'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    winner = Column(Boolean)  # Победил ли игрок в игре
    total_clicks = Column(Integer, default=0)
    successful_clicks = Column(Integer, default=0)
    failed_clicks = Column(Integer, default=0)
    color = Column(String)  # Цвет игрока в игре

    user = relationship('User', back_populates='game_statistics')
    game = relationship('Game', back_populates='game_statistics')
