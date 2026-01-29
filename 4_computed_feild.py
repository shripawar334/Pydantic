from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict


class patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int 
    weight: float 
    height: float
    married: bool
    allergies: List[str]       
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        height_in_meters = self.height / 100  # converting cm to meters
        bmi = self.weight / (height_in_meters ** 2)
        return round(bmi, 2)

      
def insert_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print("Patient data inserted successfully.")


def update_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(f"Patient BMI: {patient.calculate_bmi}")
    print("Patient data updated successfully.")


patient_info = {'name': 'John Doe', 'email': 'doe@icici.com', 'age': 65, 'weight': 20, 'height': 170, 'married': False, 'allergies': ['peanuts', 'penicillin'], 'contact_details': {'phone': '123-456-7890', 'email': 'john.doe@example.com', 'emergency_contact': '987-654-3210'}}


patient1 = patient(**patient_info)
# insert_patient_data(patient1)
update_patient_data(patient1)