from typing import List, Any

movies: List[Any] = [
    {'id': 1, 'name': 'clube da luta'}, 
    {'id': 2, 'name': 'efeito borboleta'}
]
class MovieRepository:
  def __init__(self):
    pass

  def findAll(self):
    return movies
  
  def findById(self, id: int):
    return next((m for m in movies if m['id'] == id), None)

  def create(self, movie_data: dict):
    movies.append(movie_data)
    return movies
