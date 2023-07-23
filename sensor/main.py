from typing import Optional, Union

from fastapi import FastAPI ,Depends

from sqlalchemy.orm import Session


from . import models,schemas

from .database import SessionLocal,engine


models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

   


app = FastAPI()

@app.get("/")
def read_root():
    return "Server Is Running"


@app.get("/sensors/{sensor_id}")
def read_item(sensor_id: int, location: Union[str, None] = None):
    return {"sensor_id": sensor_id, "location": location,"temprature":'20'}

@app.post("/sensor")
def create_sensor(request:schemas.Sensor,db:Session=Depends(get_db)):
    new_sensor=models.Sensor(id=request.id,temprature=request.temprature,location=request.location,status=request.status)
    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)
    return new_sensor

@app.get('/sensors')
def all(db:Session=Depends(get_db)):
    sensors= db.query(models.Sensor).all()
    return sensors


@app.get('/sensors/{id}')
def show(id:int,db:Session=Depends(get_db)):
    sensor= db.query(models.Sensor).filter(models.Sensor.id == id).first()
    return sensor