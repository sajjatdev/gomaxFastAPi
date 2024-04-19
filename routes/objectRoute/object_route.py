from fastapi import APIRouter,WebSocket,WebSocketDisconnect,Depends
from datetime import datetime
from sqlalchemy.orm import Session
from database.db import get_db,Base,engine
from model.object_position_model import  object_position_table
from sqlalchemy import inspect
from routes.objectRoute.schema.location_schema import  LocationSchema, ObjectCreateSchema


objectRoute=APIRouter()


@objectRoute.post('/object_db/create')
async def object_db_create(data:ObjectCreateSchema,db:Session=Depends(get_db)):
       try:
           # if Object Table is Exist or not
           inspector = inspect(engine)
           if "gomax_object_"+data.imei not in inspector.get_table_names(): 
               object_base,_=object_position_table(table_name=f"gomax_object_{data.imei}")
               object_base.metadata.create_all(bind=engine)

           return {"detail":"Successfully object table created"}   
                
       except:
              print("Error")

@objectRoute.websocket('/object/position/listener')
async def wp_socket(ws:WebSocket,db:Session=Depends(get_db)):
             try:
               await ws.accept()
               while True:
                  
                  object_position = await ws.receive_json()
                  if object_position:
                        
                        data= LocationSchema(**object_position)

                        _,object_location_model = object_position_table(table_name=f"gomax_object_{data.object_imei}")     
                        instance=object_location_model()
                        instance.object_imei=data.object_imei
                        instance.lat=data.lat
                        instance.lng=data.lng
                        instance.params=data.params
                        instance.angle=data.angle
                        instance.speed=data.speed
                        instance.dt_tracker=data.dt_tracker
                        instance.dt_server=data.dt_server

                        db.add(instance)
                        db.commit()
                        db.refresh(instance)

                        await ws.send_json({'detail':'Successfully data created'})


             except WebSocketDisconnect:
                     
                     ws.close()







