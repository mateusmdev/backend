from pydantic import BaseModel

class MovieSchema(BaseModel):
  id: int
  name: str
  teste: str