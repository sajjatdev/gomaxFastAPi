from fastapi import FastAPI
from routes.objectRoute.object_route import objectRoute

app=FastAPI(title="Gomax Object Data")

app.include_router(objectRoute,prefix='/api/v1')