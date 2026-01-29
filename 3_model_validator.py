from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional, Annotated

# model validator is used to validate the entire model after all feilds are validated
# it takes the entire model as input and can access all feilds of the model
# it is one of the important use cases of model validator is to validate feilds based on other feilds

class patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int 
    weight: float 
    married: bool
    allergies: List[str]       
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients over 60 years old.')
        return model
            

  
def insert_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print("Patient data inserted successfully.")

def update_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print("Patient data updated successfully.")

patient_info = {'name': 'John Doe', 'email': 'doe@icici.com', 'age': 65, 'weight': 20, 'married': False, 'allergies': ['peanuts', 'penicillin'], 'contact_details': {'phone': '123-456-7890', 'email': 'john.doe@example.com', 'emergency_contact': '987-654-3210'}}

patient1 = patient(**patient_info)
# insert_patient_data(patient1)
update_patient_data(patient1)