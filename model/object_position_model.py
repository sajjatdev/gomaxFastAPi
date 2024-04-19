from sqlalchemy import Boolean, Column, Integer, String,Float,JSON,DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


def object_position_table(table_name:str):
    Base = declarative_base()
    class ObjectDataModel(Base):
        __tablename__ = table_name

        id = Column(Integer, primary_key=True, index=True)
        object_imei = Column(String)
        dt_tracker = Column(String)
        dt_server = Column(String)
        lat = Column(Float)
        lng = Column(Float)
        speed = Column(Integer)
        angle = Column(Integer)
        params=Column(JSON)
    return Base,ObjectDataModel    
