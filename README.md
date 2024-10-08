# API de Gestión de Pacientes

Este documento describe los endpoints disponibles en la API de gestión de pacientes.

## Endpoints
![Imagen de la api](Readme1.png)

## Schemas

![Esquemas](Readme2.png)

## Instalación y Ejecución

Para instalar y ejecutar la API de gestión de pacientes, sigue estos pasos:

### Requisitos previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Agregar el archivo .env que posee las llaves para poder conectarse a la base de datos.

### Instalación

1. Clona el repositorio de la API en tu máquina local.
2. Navega hasta el directorio del proyecto en tu terminal.
3. Crea un entorno virtual de Python para aislar las dependencias del proyecto:
   ```bash
   python -m venv venv
   ```
4. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS o Linux:
     ```bash
     source venv/bin/activate
     ```
5. Instala las dependencias del proyecto utilizando el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución

1. Asegúrate de tener el entorno virtual activado.
2. Ejecuta la API utilizando uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   - `main` es el nombre del archivo Python que contiene la inicialización de la API (en este caso, `main.py`).
   - `app` es el objeto de la aplicación FastAPI.
   - `--reload` reinicia automáticamente el servidor cuando se realizan cambios en el código.

3. La API estará disponible en `http://localhost:8000`.

4. Puedes acceder a la documentación interactiva de Swagger en `http://localhost:8000/docs`.

Ahora puedes comenzar a utilizar la API de gestión de pacientes.

### 1. Obtener Pacientes

- **Método:** `GET`
- **Ruta:** `/pacientes`
- **Descripción:** Recupera una lista de pacientes. Puedes especificar el número máximo de pacientes a devolver mediante el parámetro `numero`.
- **Parámetros de consulta:**
  - `numero` (opcional): Número máximo de pacientes a devolver. Por defecto es 15.
- **Respuesta Exitosa (200 OK):**
  - **Tipo:** `List[Paciente]`
  - **Ejemplo:**
    ```json
    [
      {
        "nombre": "Juan",
        "nombre2": "Carlos",
        "apellido1": "Pérez",
        "apellido2": "Gómez",
        "documento": "123456789",
        "bloque": "A",
        "especialidad": "Cardiología",
        "proceso": "Consulta",
        "tiempo": "12:00:00"
      },
      ...
    ]
    ```

### 2. Agregar Paciente

- **Método:** `POST`
- **Ruta:** `/pacientes`
- **Descripción:** Agrega un nuevo paciente a la base de datos.
- **Cuerpo de la Solicitud:**
  - **Tipo:** `Paciente`
  - **Ejemplo:**
    ```json
    {
      "nombre": "Ana",
      "nombre2": "María",
      "apellido1": "Gómez",
      "apellido2": "Martínez",
      "documento": "987654321",
      "bloque": "B",
      "especialidad": "Neurología",
      "proceso": "Revisión",
      "tiempo": "15:30:00"
    }
    ```
- **Respuesta Exitosa (201 Created):**
  - **Tipo:** `Paciente`
  - **Ejemplo:**
    ```json
    {
      "nombre": "Ana",
      "nombre2": "María",
      "apellido1": "Gómez",
      "apellido2": "Martínez",
      "documento": "987654321",
      "bloque": "B",
      "especialidad": "Neurología",
      "proceso": "Revisión",
      "tiempo": "15:30:00"
    }
    ```

### 3. Obtener Paciente por ID

- **Método:** `GET`
- **Ruta:** `/paciente/byID`
- **Descripción:** Recupera un paciente específico por su documento de identificación.
- **Parámetros de Consulta:**
  - `documento` (requerido): Documento de identificación del paciente.
- **Respuesta Exitosa (200 OK):**
  - **Tipo:** `Paciente`
  - **Ejemplo:**
    ```json
    {
      "nombre": "Juan",
      "nombre2": "Carlos",
      "apellido1": "Pérez",
      "apellido2": "Gómez",
      "documento": "123456789",
      "bloque": "A",
      "especialidad": "Cardiología",
      "proceso": "Consulta",
      "tiempo": "12:00:00"
    }
    ```
- **Respuesta de Error (404 Not Found):**
  - **Detalle:** "Paciente no encontrado"

### 4. Actualizar Paciente

- **Método:** `PUT`
- **Ruta:** `/pacientes`
- **Descripción:** Actualiza la información de un paciente existente.
- **Cuerpo de la Solicitud:**
  - **Tipo:** `Paciente`
  - **Ejemplo:**
    ```json
    {
      "nombre": "Juan",
      "nombre2": "Carlos",
      "apellido1": "Pérez",
      "apellido2": "Gómez",
      "documento": "123456789",
      "bloque": "A",
      "especialidad": "Cardiología",
      "proceso": "Consulta",
      "tiempo": "12:00:00"
    }
    ```
- **Respuesta Exitosa (200 OK):**
  - **Tipo:** `Paciente`
  - **Ejemplo:**
    ```json
    {
      "nombre": "Juan",
      "nombre2": "Carlos",
      "apellido1": "Pérez",
      "apellido2": "Gómez",
      "documento": "123456789",
      "bloque": "A",
      "especialidad": "Cardiología",
      "proceso": "Consulta",
      "tiempo": "12:00:00"
    }
    ```

### 5. Eliminar Paciente

- **Método:** `DELETE`
- **Ruta:** `/pacientes`
- **Descripción:** Elimina un paciente de la base de datos basado en el documento de identificación.
- **Parámetros de Consulta:**
  - `documento` (requerido): Documento de identificación del paciente.
- **Respuesta Exitosa (200 OK):**
  - **Tipo:** `dict`
  - **Ejemplo:**
    ```json
    {
      "detail": "Usuario eliminado exitosamente"
    }
    ```
- **Respuesta de Error (404 Not Found):**
  - **Detalle:** "Paciente no encontrado"

## Estructura del Objeto Paciente

El objeto `Paciente` tiene el siguiente formato:

- **nombre**: `str` - Primer nombre del paciente.
- **nombre2**: `str` - Segundo nombre del paciente (opcional).
- **apellido1**: `str` - Primer apellido del paciente.
- **apellido2**: `str` - Segundo apellido del paciente (opcional).
- **documento**: `str` - Documento de identificación del paciente.
- **bloque**: `str` - Bloque o ubicación del paciente.
- **especialidad**: `str` - Especialidad médica del paciente.
- **proceso**: `str` - Proceso asociado con el paciente.
- **tiempo**: `time` - Hora asociada con el paciente.

