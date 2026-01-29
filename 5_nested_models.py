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

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address)
print(patient1.address.state)
print(patient1.address.pin)

# imp points of nested models
# 1. Nested models allow you to create complex data structures by embedding one model within another
# 2. You can validate and serialize/deserialize nested data structures easily using Pydantic
# 3. Nested models help in organizing and structuring your data better, making it more readable and maintainable
# 4. You can access nested model attributes using dot notation, making it easy to work with deeply nested data
# 5. Nested models can be reused across different parent models, promoting code reusability and consistency.