from fastapi import FastAPI, File, UploadFile, Request
from pydantic import BaseModel
import os

app = FastAPI()

class FileRequest(BaseModel):
    name: str
    content: str

@app.get("/files")
async def prueba_root():
    return {"message": "Accediste al endpoint de prueba"}


@app.post("/files")
async def create_file(request: FileRequest):
    """ 
    Crea un archivo con el nombre y contenido proporcionado en el cuerpo de la solicitud. Lo guarda en la carpeta files
    """
    with open(f"files/{request.name}", "w") as f:
        f.write(request.content)
        
    return {"message": "Archivo creado exitosamente"}


@app.get("/files/{file_name}")
async def read_file(file_name: str):
    """
    Lee el contenido de un archivo en la carpeta files.
    """
    try:
        with open(f"files/{file_name}", "r") as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return {"error": "Archivo no encontrado"}, 404