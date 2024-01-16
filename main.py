from fastapi import FastAPI,WebSocket,WebSocketDisconnect,Depends
from typing import Dict
from sqlalchemy.orm import Session
from Schema.device_schema import DeviceSchema
from Schema.location_schema import LocationSchema
from database.db import get_db,Base,engine
from model.imei_model import Device, Location


# Database Table create section
Base.metadata.create_all(bind=engine)

app=FastAPI()


con_list:Dict[str,WebSocket]={}
@app.websocket('/connect')
async def wp_socket(ws:WebSocket):
             try:

               await ws.accept()
               con_list["client"]= ws

               while True:
                   await ws.receive_json()

             except WebSocketDisconnect:
                     del con_list["client"]
                     ws.close()

@app.post('/location/create')
async def location_create(data:LocationSchema,db:Session=Depends(get_db)):
      
       try:
    
           await con_list["client"].send_json({'lat':data.lat,"long":data.long,'dt':data.dt,'imei':data.imei,'speed':data.speed})
           
           location_data=Location(**data.dict())
           db.add(location_data) 
           db.commit()
           db.refresh(location_data)

       except:
              print("Error")       
       
       return {"message":"Done"}



@app.post('/imei/create')
async def create_device(data:DeviceSchema,db:Session=Depends(get_db)):
       device_data=  Device(**data.dict())

       db.add(device_data)
       db.commit()
       db.refresh(device_data)

       return {"message":"Successfully created"}