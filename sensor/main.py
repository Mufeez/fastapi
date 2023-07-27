from typing import Optional, Union

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
def read_root():
    return "Server Is Running"

@app.post("/sensor", response_model=schemas.Sensor)
def create_sensor(request: schemas.Sensor, db: Session = Depends(get_db)):
    new_sensor = models.Sensor(id=request.id, temprature=request.temprature, location=request.location, status=request.status)
    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)
    return new_sensor

@app.get('/sensors', response_model=list[schemas.Sensor])
def all(db: Session = Depends(get_db)):
    sensors = db.query(models.Sensor).all()
    return sensors

@app.get('/sensors/{id}', response_model=schemas.Sensor)
def show(id: int, db: Session = Depends(get_db)):
    sensor = db.query(models.Sensor).filter(models.Sensor.id == id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor

@app.put('/sensors/{id}', response_model=schemas.Sensor)
def update_sensor(id: int, request: schemas.Sensor, db: Session = Depends(get_db)):
    sensor = db.query(models.Sensor).filter(models.Sensor.id == id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    for key, value in request.dict(exclude_unset=True).items():
        setattr(sensor, key, value)
    db.commit()
    db.refresh(sensor)
    return sensor

@app.delete('/sensors/{id}', response_model=schemas.Sensor)
def delete_sensor(id: int, db: Session = Depends(get_db)):
    sensor = db.query(models.Sensor).filter(models.Sensor.id == id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    db.delete(sensor)
    db.commit()
    return sensor
