from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int 
    weight: float 
    married: bool
    allergies: List[str]       
    contact_details: Dict[str, str]

# feild validator is class method that is used to validate a specific feild

    @field_validator('email')
    @classmethod
    def validate_email_domain(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name= value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f'Email domain must be one of the following: {valid_domains}')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    # the default value of mode is after
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0<value < 100:
            return value
        else:
            raise ValueError('Age must be between 0 and 100')
        
    
def insert_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print("Patient data inserted successfully.")

def update_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print("Patient data updated successfully.")

patient_info = {'name': 'John Doe', 'email': 'doe@icici.com', 'age': 30, 'weight': 20, 'married': False, 'allergies': ['peanuts', 'penicillin'], 'contact_details': {'phone': '123-456-7890', 'email': 'john.doe@example.com'}}

patient1 = patient(**patient_info)
# insert_patient_data(patient1)
update_patient_data(patient1)