from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Diccionarios simulados como bases de datos
db_pacientes = {}
db_profesionales = {}
db_citas = {}
db_facturas = {}

# Modelo Pydantic para Pacientes
class PacienteModel(BaseModel):
    id: int
    name: str
    gender: str
    phone: str
    service: str

# Modelo Pydantic para Profesionales de la Salud
class ProfesionalModel(BaseModel):
    id: int
    name: str
    specialty: str
    phone: str
    address: str

# Modelo Pydantic para Citas
class CitaModel(BaseModel):
    id: int
    patient_id: int
    professional_id: int
    datetime: str
    notes: Optional[str] = None

# Modelo Pydantic para Facturas
class FacturaModel(BaseModel):
    id: int
    patient_id: int
    amount: float
    details: str

# Endpoint para crear un nuevo paciente
@app.post("/pacientes/", response_model=PacienteModel)
def create_paciente(paciente: PacienteModel):
    if paciente.id in db_pacientes:
        raise HTTPException(status_code=400, detail="Paciente ya registrado")
    db_pacientes[paciente.id] = paciente
    return paciente

# Endpoint para leer todos los pacientes
@app.get("/pacientes/", response_model=List[PacienteModel])
def read_pacientes():
    return list(db_pacientes.values())

# Endpoint para leer un paciente específico por ID
@app.get("/pacientes/{paciente_id}", response_model=PacienteModel)
def read_paciente(paciente_id: int):
    if paciente_id not in db_pacientes:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return db_pacientes[paciente_id]

# Endpoint para actualizar un paciente por ID
@app.put("/pacientes/{paciente_id}", response_model=PacienteModel)
def update_paciente(paciente_id: int, paciente: PacienteModel):
    if paciente_id not in db_pacientes:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    db_pacientes[paciente_id] = paciente
    return paciente

# Endpoint para eliminar un paciente por ID
@app.delete("/pacientes/{paciente_id}")
def delete_paciente(paciente_id: int):
    if paciente_id not in db_pacientes:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    del db_pacientes[paciente_id]
    return {"message": "Paciente eliminado exitosamente"}

# Endpoint para crear un nuevo profesional de la salud
@app.post("/profesionales/", response_model=ProfesionalModel)
def create_profesional(profesional: ProfesionalModel):
    if profesional.id in db_profesionales:
        raise HTTPException(status_code=400, detail="Profesional ya registrado")
    db_profesionales[profesional.id] = profesional
    return profesional

# Endpoint para leer todos los profesionales
@app.get("/profesionales/", response_model=List[ProfesionalModel])
def read_profesionales():
    return list(db_profesionales.values())

# Endpoint para leer un profesional específico por ID
@app.get("/profesionales/{profesional_id}", response_model=ProfesionalModel)
def read_profesional(profesional_id: int):
    if profesional_id not in db_profesionales:
        raise HTTPException(status_code=404, detail="Profesional no encontrado")
    return db_profesionales[profesional_id]

# Endpoint para actualizar un profesional por ID
@app.put("/profesionales/{profesional_id}", response_model=ProfesionalModel)
def update_profesional(profesional_id: int, profesional: ProfesionalModel):
    if profesional_id not in db_profesionales:
        raise HTTPException(status_code=404, detail="Profesional no encontrado")
    db_profesionales[profesional_id] = profesional
    return profesional

# Endpoint para eliminar un profesional por ID
@app.delete("/profesionales/{profesional_id}")
def delete_profesional(profesional_id: int):
    if profesional_id not in db_profesionales:
        raise HTTPException(status_code=404, detail="Profesional no encontrado")
    del db_profesionales[profesional_id]
    return {"message": "Profesional eliminado exitosamente"}

# Endpoint para crear una nueva cita
@app.post("/citas/", response_model=CitaModel)
def create_cita(cita: CitaModel):
    if cita.id in db_citas:
        raise HTTPException(status_code=400, detail="Cita ya registrada")
    db_citas[cita.id] = cita
    return cita

# Endpoint para leer todas las citas
@app.get("/citas/", response_model=List[CitaModel])
def read_citas():
    return list(db_citas.values())

# Endpoint para leer una cita específica por ID
@app.get("/citas/{cita_id}", response_model=CitaModel)
def read_cita(cita_id: int):
    if cita_id not in db_citas:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return db_citas[cita_id]

# Endpoint para actualizar una cita por ID
@app.put("/citas/{cita_id}", response_model=CitaModel)
def update_cita(cita_id: int, cita: CitaModel):
    if cita_id not in db_citas:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    db_citas[cita_id] = cita
    return cita

# Endpoint para cancelar una cita por ID
@app.delete("/citas/{cita_id}")
def delete_cita(cita_id: int):
    if cita_id not in db_citas:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    del db_citas[cita_id]
    return {"message": "Cita cancelada exitosamente"}

# Endpoint para crear una nueva factura
@app.post("/facturas/", response_model=FacturaModel)
def create_factura(factura: FacturaModel):
    if factura.id in db_facturas:
        raise HTTPException(status_code=400, detail="Factura ya registrada")
    db_facturas[factura.id] = factura
    return factura

# Endpoint para leer todas las facturas
@app.get("/facturas/", response_model=List[FacturaModel])
def read_facturas():
    return list(db_facturas.values())

# Endpoint para leer una factura específica por ID
@app.get("/facturas/{factura_id}", response_model=FacturaModel)
def read_factura(factura_id: int):
    if factura_id not in db_facturas:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return db_facturas[factura_id]

# Endpoint para actualizar una factura por ID
@app.put("/facturas/{factura_id}", response_model=FacturaModel)
def update_factura(factura_id: int, factura: FacturaModel):
    if factura_id not in db_facturas:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    db_facturas[factura_id] = factura
    return factura

# Endpoint para eliminar una factura por ID
@app.delete("/facturas/{factura_id}")
def delete_factura(factura_id: int):
    if factura_id not in db_facturas:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    del db_facturas[factura_id]
    return {"message": "Factura eliminada exitosamente"}
