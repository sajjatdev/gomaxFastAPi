from fastapi import FastAPI,WebSocket,WebSocketDisconnect
from typing import Dict
from pydantic import BaseModel
app=FastAPI()


class Location(BaseModel):
       lat:str
       long:str

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

@app.post('/send')
async def send_data(data:Location):
      
       try:
             await con_list["client"].send_json({'lat':data.lat,"long":data.long})
       except:
              print("Error")       
       
       return {"message":"Done"}
   