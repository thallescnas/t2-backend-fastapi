from pydantic import BaseModel
from typing import Optional

class CarRegister(BaseModel):
    modelo: str
    ano: int
    fabricante: str
    usado: bool

class CarResponse(BaseModel):
    modelo: str
    ano: int
    fabricante: str
    id: int

class CarUpdate(BaseModel):
    modelo: Optional[str] = None
    ano: Optional[int] = None
    fabricante: Optional[str] = None 
    usado: bool

class Config:
    from_attributes: True #Ler ORM

