from pydantic import BaseModel

class DeviceSchema(BaseModel):
       name:str
       phone:str
       imei:str  