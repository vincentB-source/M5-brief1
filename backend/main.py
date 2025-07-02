from fastapi import FastAPI
from loguru import logger
from pydantic import BaseModel

from os.path import join as join
import json

app = FastAPI()
logger.add("logs/prediction.log")

class Nombre(BaseModel):
    nombre: int
    
@app.get("/")
async def root():
    logger.info("Route '/' appelée.")
    return {"message": "Hello World!"}

@app.get("/health")
async def health():
    logger.info("Route '/health' appelée.")
    return {"message": "OK!"}

@app.post("/calcul/")
async def faire_calcul(nombre: Nombre) -> dict[str, str]:
    logger.info("Route '/faire_calcul/' (POST) appelée.")

    carre = nombre.nombre**2
    
    logger.info(f"C'est carré !!! on a fait le calcul pour {nombre.nombre} : {carre}")

    return {"message": f'Alors pour {nombre.nombre} nous trouvons : {carre}'}
