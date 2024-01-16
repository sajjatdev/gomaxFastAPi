from sqlalchemy import Boolean, Column, Integer, String,Float
from database.db import Base


class Device(Base):
    __tablename__ = "device"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    imei = Column(String, unique=True, index=True)
    phone = Column(String)
   
class Location(Base):
    __tablename__ = "location"
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    lat = Column(Float)
    long = Column(Float)
    speed=Column(Integer)
    dt_date = Column(String)
    device_imei = Column(String)
