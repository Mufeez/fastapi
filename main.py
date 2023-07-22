from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Server Is Running"


@app.get("/sensors/{sensor_id}")
def read_item(sensor_id: int, location: Union[str, None] = None):
    return {"sensor_id": sensor_id, "location": location,"temprature":'20'}

