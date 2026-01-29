from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# this is schema for patient data that means to validate the patient data before inserting or updating in the database
# List is used for two level validation like allergies is a list of strings
# Dict is used for key value pair validation like contact_details is a dictionary with string keys and string values
class patient(BaseModel):
    # id: int = Field(..., description="Unique identifier for the patient")
    # name: str = Field(..., min_length=2, max_length=50, description="Full name of the patient")
    name: Annotated[str, Field(min_length=2, max_length=50, description="Full name of the patient",     example="John Doe")] 
    email: EmailStr
    Linkdin_profile: Optional[AnyUrl] = None
    age: int 
    weight: float = Field(..., gt=0, description="Weight of the patient in kilograms")
    # married: bool
    married: Optional[bool] = None
    # allergies: List[str] 
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

# in pydantic all feilds are required by degault

def insert_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print("Patient data inserted successfully.")

def update_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print("Patient data updated successfully.")


# patient_info = {'name': 'John Doe', 'age': 'thirty'}-> This will raise a validation error due to age being a string instead of an integer
patient_info = {'name': 'John Doe', 'email': 'doe@gmail.com', 'age': 30, 'weight': 20, 'married': False, 'allergies': ['peanuts', 'penicillin'], 'contact_details': {'phone': '123-456-7890', 'email': 'john.doe@example.com'}}

patient1 = patient(**patient_info)
# insert_patient_data(patient1)
update_patient_data(patient1)