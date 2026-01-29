from pydantic import BaseModel

class Address(BaseModel):
    
    city: str
    state: str
    pin: str

class patient(BaseModel):
    
    name: str
    gender: str
    age: int 
    address: 'Address'  # Forward reference to Address model


address_dict = {'city': 'pune', 'state': 'maharashtra', 'pin': '10001'}

address1= Address(**address_dict)

patient_dict = {'name': 'John Doe', 'gender': 'Male', 'age': 30, 'address': address1}

patient1 = patient(**patient_dict)

# temp = patient1.model_dump_json()
temp = patient1.model_dump(include=['name', 'age'])
temp = patient1.model_dump(exclude=['name', 'age'])
print(temp)
print(type(temp))