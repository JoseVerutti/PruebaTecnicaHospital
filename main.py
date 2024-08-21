from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from endpoints.pacientes import endpointPacientes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # Agrega la URL de tu frontend
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

app.include_router(endpointPacientes)

@app.get("/")
def returnDOCS():
    return RedirectResponse("/docs")
