from fastapi import Depends, HTTPException
from service.movie_service import MovieService
from model.movie_schema import MovieSchema

class MovieController:
  def __init__(self, service: MovieService = Depends(MovieService)):
    self.service = service
  
  def get_movies(self, movie_id: int = None):
    result = self.service.get_movies(movie_id)
  
    if result is None:
      response = {"message": "Movie not found", "status": 404}
      raise HTTPException(status_code=response["status"], detail=response)
      
    return result

    
  def add_movie(self, movie: MovieSchema):
    return self.service.add_movie(movie)