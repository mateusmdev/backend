from pydantic import BaseModel
from typing import List, Any

class MovieRepository(BaseModel):

  movies: List[Any] = [{'id': 1, 'name': 'clube da luta'}, {'id': 2, 'name': 'efeito borboleta'}]

  def findAll(self):
    return self.movies
  
  def findById(self, id: int):
    return self.movies[id]
