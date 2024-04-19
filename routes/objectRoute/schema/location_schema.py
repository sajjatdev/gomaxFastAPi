from pydantic import BaseModel
from typing import Dict

class ObjectCreateSchema(BaseModel):
       imei:str

class LocationSchema(BaseModel):
       dt_server:str
       dt_tracker:str
       lat:float
       lng:float
       angle:int
       speed:int
       params:Dict
       object_imei:str


