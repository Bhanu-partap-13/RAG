import json
import uuid
from typing import Annotated, Literal
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field

app = FastAPI()

class Patient(BaseModel):
    name: str = Field(..., description="Name of the patient")
    city: str = Field(..., description="City of the patient")
    age: int = Field(..., description="Age of the patient")
    gender: Literal['male', 'female', 'other'] = Field(..., description="Gender of Patient")
    height: float = Field(..., gt=0, description="Height of Patient in meters")
    weight: float = Field(..., gt=0, description="Weight of Patient in kg")

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'underweight'
        elif 18.5 <= self.bmi < 25:
            return 'normal'
        elif 25 <= self.bmi < 30:
            return 'overweight'
        elif 30 <= self.bmi < 40:
            return 'obesity'
        else:
            return 'extreme obesity'

def load_data():
    try:
        with open('patients.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open('patients.json', 'w') as file:
        json.dump(data, file, indent=4)

@app.get('/')
def read_root():
    return {"message": "Welcome to the Patient API! Go to /docs to see the documentation."}


@app.post('/create')
def create_patient(patient: Patient):
    # Existing data ko load krenge
    data = load_data()
    
    # 1. Unique ID generate karenge
    new_id = str(uuid.uuid4())
    
    # 2. Patient ka data dictionary (JSON) format mein lenge
    patient_data = patient.model_dump()
    
    # 3. Naye generated ID ko JSON data mein daal denge
    patient_data["id"] = new_id
    
    # 4. Data dictionary mein new patient add karenge
    data[new_id] = patient_data
    
    # 5. Updated data ko file me save krenge
    save_data(data)
    
    # Response me new ID bhi return kr dete h
    return JSONResponse(status_code=201, content={
        "message": "Patient created successfully",
        "id": new_id
    })
