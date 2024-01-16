from pydantic import BaseModel

class LocationSchema(BaseModel):
       lat:float
       long:float
       speed:int
       dt_date:str
       device_imei:str
