from pydantic import (BaseModel, ValidationError, Field, PositiveFloat, PositiveInt)
from typing import Optional


# class LLMresp(BaseModel):
#     id: int = Field(ge=0)
#     intent: str
#     confidence: float = Field(ge=0, le=1)
#     entities: Optional[dict]
    
# k = {
#     'id':123,
#     'intent':"research",
#     'confidence':0.4,
#     'entities': {
#         'k_top':100,
#         'temperture':0.9
#     },
# }

# try:
#     data = LLMresp(**k)  
#     print(data)
# except ValidationError as e:
#     print(e.errors())


class Product(BaseModel):
    id: PositiveInt
    name: str
    price: PositiveFloat
    description : str = Field(min_length=2)
    quantity: PositiveInt


