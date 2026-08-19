from pydantic import BaseModel

class Patient(BaseModel):
    # ek pydantic model jiske andar data ayega from user
    name : str
    age : int
    gender : str

def insert_patient(patient: Patient):
    print(patient.name) 
    print(patient.age)
    print(patient.gender)
    print('Inserted')

patient_info = {"name":'Awaiz' , "age":21, "gender":'Male'}

patient1 = Patient(**patient_info)

insert_patient(patient1)