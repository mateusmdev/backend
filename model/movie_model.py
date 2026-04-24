from sqlalchemy import Column, Integer, String, Float
from database.config import Base

class MovieModel(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    duration = Column(Float, nullable=False)
    rate = Column(Float, nullable=False)
