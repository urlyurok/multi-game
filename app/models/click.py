from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db import Base


class Click(Base):
    __tablename__ = 'clicks'

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    x = Column(Integer)  # Координата по оси X
    y = Column(Integer)  # Координата по оси Y
    successful = Column(Boolean)  # Успешный ли клик (True или False)

    game = relationship('Game', back_populates='clicks')
    user = relationship('User', back_populates='clicks')
