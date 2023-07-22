from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, unique=True, index=True)
    temprature = Column(Integer)
    status = Column(Boolean, default=True)

   