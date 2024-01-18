from pydantic import BaseModel
from typing import Dict
class LocationSchema(BaseModel):
       lat:float
       long:float
       speed:int
       dt_date:str
       device_imei:str
       angle:int
       params:Dict
