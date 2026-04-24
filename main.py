from fastapi import FastAPI
from router import movie_router

app = FastAPI()

app.include_router(movie_router.router, prefix='/filmes')

@app.get("/")
async def root():
    return {"message": "Hello World"}