from fastapi import FastAPI,WebSocket,WebSocketDisconnect
from typing import Dict
from pydantic import BaseModel
app=FastAPI()


class Location(BaseModel):
       lat:str
       long:str

con_list:Dict[str,WebSocket]={}


@app.post('/send')
async def send_data(data:Location):
       con_list["1"].send_json({'lat':data.lat,"long":data.long})

@app.websocket('/connect')
async def wp_socket(ws:WebSocket):
             try:

               await ws.accept()
               con_list["1"]=ws

               while True:
                    pass
             except WebSocketDisconnect:
                     del con_list["1"]
                     ws.close()


   