from beanie import Document
from typing import Literal,Self
from enum import IntEnum
from pydantic import BaseModel,EmailStr,Field,model_validator
from pydantic_core import PydanticCustomError

class newAdminType(BaseModel):
    name:str=Field(min_length=3,max_length=15)
    email:EmailStr=Field(max_length=40)
    password:str=Field(min_length=3,max_length=30)

class newUserType(BaseModel):
    name:str=Field(min_length=3,max_length=15)
    password:str=Field(min_length=3,max_length=30)
    accessLevel:Literal[1,2,3]|None=Field(default=1)


class UserSchema(Document):
    name: str=Field(min_length=3,max_length=15)
    email:EmailStr|None =Field(default=None,max_length=40)
    emailIsConfirmed:bool|None=None
    confirmationCode:str|None=None
    password:str=Field(min_length=6,max_length=100)
    accessLevel:Literal[1,2,3]
    date:str

    class Settings:
        name = "users"

class LoginType(BaseModel):
     name:str=Field(min_length=3,max_length=15)
     password:str=Field(min_length=3,max_length=30)
     
class ConfirmationType(BaseModel):
     name:str=Field(min_length=3,max_length=15)
     code:str=Field(min_length=3,max_length=50)
     