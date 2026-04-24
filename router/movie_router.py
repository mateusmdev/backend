from fastapi import APIRouter, Depends, Request
from controller.movie_controller import MovieController
from model.movie_schema import MovieSchema

router = APIRouter()

controller = MovieController()

@router.get('/')
def get_movies(controller: MovieController = Depends(MovieController)):
  return controller.get_movies()

@router.get('/{movie_id}/')
def get_movie(movie_id: int, controller: MovieController = Depends(MovieController)):
  return controller.get_movies(movie_id)

@router.post('/')
def add_movie(movie: MovieSchema, controller: MovieController = Depends(MovieController)):
  return controller.add_movie(movie)