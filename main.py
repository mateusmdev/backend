from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from router import movie_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movie_router.router, prefix='/filmes')

@app.exception_handler(Exception)
async def handler_geral(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Erro interno customizado"}
    )