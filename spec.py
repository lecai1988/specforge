from pydantic import BaseModel
 
class PartSpec(BaseModel):
    name: str
    length: float
    width: float
    thickness: float
