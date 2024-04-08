from pydantic import BaseModel


class Course(BaseModel):
    name: str
    location: str
    holes: int