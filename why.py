from pydantic import BaseModel

# this is schema for patient data that means to validate the patient data before inserting or updating in the database
class patient(BaseModel):
    # id: int = Field(..., description="Unique identifier for the patient")
    name: str  
    age: int 
    # weight: float 

def insert_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print("Patient data inserted successfully.")

def update_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print("Patient data updated successfully.")


# patient_info = {'name': 'John Doe', 'age': 'thirty'}-> This will raise a validation error due to age being a string instead of an integer
patient_info = {'name': 'John Doe', 'age': 30}

patient1 = patient(**patient_info)
# insert_patient_data(patient1)
update_patient_data(patient1)