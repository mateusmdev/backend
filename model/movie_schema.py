from pydantic import BaseModel

class MovieSchema(BaseModel):
  name: str
  genre: str
  duration: float
  rate: float