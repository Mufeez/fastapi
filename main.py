from typing import Optional, Union

from fastapi import FastAPI

from pydantic import BaseModel

import uvicorn


class Sensor(BaseModel):
    serailNumber:int
    temprature:int
    location:str
    validity:str
    id:int
    status: Optional[bool]


app = FastAPI()


@app.get("/")
def read_root():
    return "Server Is Running"


@app.get("/sensors/{sensor_id}")
def read_item(sensor_id: int, location: Union[str, None] = None):
    return {"sensor_id": sensor_id, "location": location,"temprature":'20'}

@app.post("/sensor")
def create_sensor(sensor:Sensor):
    return sensor

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)


