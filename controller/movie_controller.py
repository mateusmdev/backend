from fastapi import Depends
from service.movie_service import MovieService
from model.movie_schema import MovieSchema

class MovieController:
  def __init__(self, service: MovieService = Depends(MovieService)):
    self.service = service
  
  def get_movies(self, movie_id: int = None):
    try:
      return self.service.get_movies(movie_id)
    except Exception as e:
      print(f"Erro ao buscar filmes: {e}")
      raise e
    
  def add_movie(self, movie: MovieSchema):
    try:
      return self.service.add_movie(movie)
    except Exception as e:
      print(f"Erro ao adicionar filme: {e}")
      raise e