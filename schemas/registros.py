from pydantic import BaseModel
from datetime import datetime, time

class Paciente(BaseModel):

    nombre : str
    nombre2 : str
    apellido1 : str
    apellido2 : str
    documento : str
    bloque : str
    especialidad : str
    proceso : str
    tiempo : int


