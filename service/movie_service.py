from fastapi import Depends
from repository.movie_repository import MovieRepository
from model.movie_schema import MovieSchema

class MovieService:
  def __init__(self, repository: MovieRepository = Depends(MovieRepository)):
    self.repository = repository

  def get_movies(self, movie_id: int = None):
    if movie_id is None:
      return self.repository.findAll()
    return self.repository.findById(int(movie_id))

  def add_movie(self, movie: MovieSchema):
    data = self.repository.create(movie.model_dump())
    return data