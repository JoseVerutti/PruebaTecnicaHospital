from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from endpoints.pacientes import endpointPacientes

app = FastAPI()

app.include_router(endpointPacientes)

@app.get("/")
def returnDOCS():
    return RedirectResponse("/docs")
