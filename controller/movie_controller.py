from pydantic import BaseModel
from fastapi import Depends, Request
from service.movie_service import MovieService

class MovieController(BaseModel):

  service: MovieService = Depends(MovieService)
  
  def get_movies(self, request: Request):
    try:
      movie_id = request.path_params.get('movie_id')
      return self.service.get_movies(movie_id)

    except Exception as e:
      print(e)
      raise e
    
    