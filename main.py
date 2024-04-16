from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from patientRegistration import Pacient, ClinicHistory
from servicesProvider import ServicesProvider
from billing import Billing

app = FastAPI()

# Diccionarios como bases de datos simuladas
db_pacientes = {}
db_profesionales = {}
db_citas = {}
db_facturas = {}

# Modelo Pydantic para Paciente
class PacienteModel(BaseModel):
    id: int
    name: str
    gender: str
    phone: str
    service: str

# Modelo Pydantic para Profesional de la Salud
class ProfesionalModel(BaseModel):
    id: int
    name: str
    specialty: str
    phone: str
    address: str

# Modelo Pydantic para Cita
class CitaModel(BaseModel):
    id: int
    patient_id: int
    professional_id: int
    datetime: str
    notes: Optional[str] = None

# Modelo Pydantic para Factura
class FacturaModel(BaseModel):
    id: int
    patient_id: int
    amount: float
    details: str

@app.post("/pacientes/", response_model=PacienteModel)
def create_paciente(paciente: PacienteModel):
    if paciente.id in db_pacientes:
        raise HTTPException(status_code=400, detail="Paciente already registered")
    db_pacientes[paciente.id] = paciente
    return paciente

@app.get("/pacientes/", response_model=List[PacienteModel])
def read_pacientes():
    return list(db_pacientes.values())

@app.get("/pacientes/{paciente_id}", response_model=PacienteModel)
def read_paciente(paciente_id: int):
    if paciente_id not in db_pacientes:
        raise HTTPException(status_code=404, detail="Paciente not found")
    return db_pacientes[paciente_id]

@app.put("/pacientes/{paciente_id}", response_model=PacienteModel)
def update_paciente(paciente_id: int, paciente: PacienteModel):
    if paciente_id not in db_pacientes:
        raise HTTPException(status_code=404, detail="Paciente not found")
    db_pacientes[paciente_id] = paciente
    return paciente

@app.delete("/pacientes/{paciente_id}")
def delete_paciente(paciente_id: int):
    if paciente_id not in db_pacientes:
        raise HTTPException(status_code=404, detail="Paciente not found")
    del db_pacientes[paciente_id]
    return {"message": "Paciente deleted successfully"}

@app.post("/profesionales/", response_model=ProfesionalModel)
def create_profesional(profesional: ProfesionalModel):
    if profesional.id in db_profesionales:
        raise HTTPException(status_code=400, detail="Profesional already registered")
    db_profesionales[profesional.id] = profesional
    return profesional

@app.get("/profesionales/", response_model=List[ProfesionalModel])
def read_profesionales():
    return list(db_profesionales.values())

@app.get("/profesionales/{profesional_id}", response_model=ProfesionalModel)
def read_profesional(profesional_id: int):
    if profesional_id not in db_profesionales:
        raise HTTPException(status_code=404, detail="Profesional not found")
    return db_profesionales[profesional_id]

@app.put("/profesionales/{profesional_id}", response_model=ProfesionalModel)
def update_profesional(profesional_id: int, profesional: ProfesionalModel):
    if profesional_id not in db_profesionales:
        raise HTTPException(status_code=404, detail="Profesional not found")
    db_profesionales[profesional_id] = profesional
    return profesional

@app.delete("/profesionales/{profesional_id}")
def delete_profesional(profesional_id: int):
    if profesional_id not in db_profesionales:
        raise HTTPException(status_code=404, detail="Profesional not found")
    del db_profesionales[profesional_id]
    return {"message": "Profesional deleted successfully"}

@app.post("/citas/", response_model=CitaModel)
def create_cita(cita: CitaModel):
    if cita.id in db_citas:
        raise HTTPException(status_code=400, detail="Cita already registered")
    db_citas[cita.id] = cita
    return cita

@app.get("/citas/", response_model=List[CitaModel])
def read_citas():
    return list(db_citas.values())

@app.get("/citas/{cita_id}", response_model=CitaModel)
def read_cita(cita_id: int):
    if cita_id not in db_citas:
        raise HTTPException(status_code=404, detail="Cita not found")
    return db_citas[cita_id]

@app.put("/citas/{cita_id}", response_model=CitaModel)
def update_cita(cita_id: int, cita: CitaModel):
    if cita_id not in db_citas:
        raise HTTPException(status_code=404, detail="Cita not found")
    db_citas[cita_id] = cita
    return cita

@app.delete("/citas/{cita_id}")
def delete_cita(cita_id: int):
    if cita_id in db_citas:
        del db_citas[cita_id]
        return {"message": "Cita cancelled successfully"}
    raise HTTPException(status_code=404, detail="Cita not found")

@app.post("/facturas/", response_model=FacturaModel)
def create_factura(factura: FacturaModel):
    if factura.id in db_facturas:
        raise HTTPException(status_code=400, detail="Factura already registered")
    db_facturas[factura.id] = factura
    return factura

@app.get("/facturas/", response_model=List[FacturaModel])
def read_facturas():
    return list(db_facturas.values())

@app.get("/facturas/{factura_id}", response_model=FacturaModel)
def read_factura(factura_id: int):
    if factura_id not in db_facturas:
        raise HTTPException(status_code=404, detail="Factura not found")
    return db_facturas[factura_id]

@app.put("/facturas/{factura_id}", response_model=FacturaModel)
def update_factura(factura_id: int, factura: FacturaModel):
    if factura_id not in db_facturas:
        raise HTTPException(status_code=404, detail="Factura not found")
    db_facturas[factura_id] = factura
    return factura

@app.delete("/facturas/{factura_id}")
def delete_factura(factura_id: int):
    if factura_id in db_facturas:
        del db_facturas[factura_id]
        return {"message": "Factura deleted successfully"}
    raise HTTPException(status_code=404, detail="Factura not found")