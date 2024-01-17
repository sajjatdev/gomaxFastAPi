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


con_list:list[WebSocket]=[]

@app.websocket('/connect/')
async def wp_socket(ws:WebSocket):
             try:

               await ws.accept()
               con_list.append(ws)

               while True:
                   await ws.receive_json()

             except WebSocketDisconnect:
                     con_list.remove(ws)
                     ws.close()
                     

@app.post('/location/create')
async def location_create(data:LocationSchema,db:Session=Depends(get_db)):
      
       try:
           for element in con_list:    

              await element.send_json({'lat':data.lat,"long":data.long,'dt':data.dt_date,'imei':data.device_imei,'speed':data.speed})
           
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