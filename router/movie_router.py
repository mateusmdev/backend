from fastapi import APIRouter, Depends, Request
from controller.movie_controller import MovieController

router = APIRouter()

@router.get('/')
def get_movies(request: Request, controller: MovieController = Depends(MovieController)):
  return controller.get_movies(request)

@router.get('/{movie_id}/')
def get_movie(request: Request, controller: MovieController = Depends(MovieController)):
  return controller.get_movies(request)

