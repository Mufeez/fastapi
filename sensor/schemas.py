
from typing import Optional
from pydantic import BaseModel

class Sensor(BaseModel):
    temprature:int
    location:str
    id:int
    status: Optional[bool]