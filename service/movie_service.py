from pydantic import BaseModel
from fastapi import Depends
from repository.movie_repository import MovieRepository

class MovieService(BaseModel):
  
  repository: MovieRepository = Depends(MovieRepository)

  def get_movies(self, movie_id: int = None):
    if movie_id == None:
      return self.repository.findAll()
    
    return self.repository.findById(int(movie_id))

  
  