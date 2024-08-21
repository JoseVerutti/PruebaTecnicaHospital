from fastapi import APIRouter
from schemas.registros import Paciente
from config.db import dynamodb as db
from functions.pacientes import *

endpointPacientes = APIRouter()

@endpointPacientes.get("/pacientes")
def getPacientes(numero : int = 15):

    response = obtenerUsuarios(db, numero)

    return response

@endpointPacientes.post("/pacientes")
def aregarPacientes(paciente:Paciente):

    response = agregarUsuario(db,paciente)

    return response

@endpointPacientes.get("/paciente/byID")
def getPaciente(documento : str):

    response = obtenerUsuarioID(db, documento)

    return response


@endpointPacientes.put("/pacientes")
def actualizarPacientes(paciente:Paciente):

    response = actualizarUsuario(db, paciente)
     
    return response

@endpointPacientes.delete("/pacientes")
def eliminarPaciente(documento:str):

    response = eliminarUsuario(db, documento)

    return response