from typing import List
from sqlalchemy.orm import Session
from database.config import SessionLocal, engine, Base
from model.movie_model import MovieModel

Base.metadata.create_all(bind=engine)

class MovieRepository:
    def __init__(self):
        self.db: Session = SessionLocal()

    def findAll(self) -> List[MovieModel]:
        return self.db.query(MovieModel).all()

    def findById(self, id: int) -> MovieModel:
        return self.db.query(MovieModel).filter(MovieModel.id == id).first()

    def create(self, movie_data: dict) -> List[MovieModel]:
        db_movie = MovieModel(**movie_data)
        self.db.add(db_movie)
        self.db.commit()
        self.db.refresh(db_movie)

        return self.findAll()

    def __del__(self):
        self.db.close()
