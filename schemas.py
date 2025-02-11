from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Student(BaseModel):
    id: int
    firstname: str
    lastname: str
    age: int
    address: str
    emailid: str
    status: int


class ReadStudent(BaseModel):
    id: int
    firstname: str
    lastname: str
    age: int
    address: str
    emailid: str
    status: int
    class Config:
        from_attributes = True


class Employee(BaseModel):
    id: int
    name: str
    email: str
    address: str
    pincode: int


class ReadEmployee(BaseModel):
    id: int
    name: str
    email: str
    address: str
    pincode: int
    class Config:
        from_attributes = True




class PutStudentId(BaseModel):
    id: str
    firstname: str
    lastname: str
    age: str
    address: str
    emailid: str
    status: str

    class Config:
        from_attributes = True

