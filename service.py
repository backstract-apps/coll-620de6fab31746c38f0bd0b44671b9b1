from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_student(db: Session):

    student_all = db.query(models.Student).all()
    student_all = [new_data.to_dict() for new_data in student_all] if student_all else student_all

    res = {
        'student_all': student_all,
    }
    return res

async def get_student_id(db: Session, id: int):

    student_one = db.query(models.Student).filter(models.Student.id == id).first() 
    student_one = student_one.to_dict() if student_one else student_one



    query = db.query(models.Student)
    query = query.filter(
        
        and_(
            models.Student.firstname != student_one
        )
    )


    user_get_api = query.all()
    user_get_api = [new_data.to_dict() for new_data in user_get_api] if user_get_api else user_get_api

    res = {
        'student_one': student_one,
    }
    return res

async def post_student(db: Session, id: int, firstname: str, lastname: str, age: int, address: str, emailid: str, status: int):

    record_to_be_added = {'emailid': emailid, 'id': id, 'firstname': firstname, 'lastname': lastname, 'age': age, 'address': address, 'status': status}
    new_student = models.Student(**record_to_be_added)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    student_data1 = new_student.to_dict()



    query = db.query(models.Student)
    query = query.filter(
        
        and_(
            models.Student.id == id
        )
    )


    student_data = query.all()
    student_data = [new_data.to_dict() for new_data in student_data] if student_data else student_data

    res = {
        'student_inserted_record': student_data1,
        'students_find': student_data,
    }
    return res

async def put_student_id(db: Session, raw_data: schemas.PutStudentId):
    id:str = raw_data.id
    firstname:str = raw_data.firstname
    lastname:str = raw_data.lastname
    age:str = raw_data.age
    address:str = raw_data.address
    emailid:str = raw_data.emailid
    status:str = raw_data.status


    student_edited_record = db.query(models.Student).filter(models.Student.id == id).first()
    for key, value in {'id': id, 'firstname': firstname, 'lastname': lastname, 'age': age, 'address': address, 'emailid': emailid, 'status': status}.items():
          setattr(student_edited_record, key, value)
    db.commit()
    db.refresh(student_edited_record)
    student_edited_record = student_edited_record.to_dict() 

    res = {
        'student_edited_record': student_edited_record,
    }
    return res

async def delete_student_id(db: Session, id: str, firstname: str, lastname: str, age: str, address: str, emailid: str, status: str):

    record_to_be_added = {'id': id, 'firstname': firstname, 'lastname': lastname, 'age': age, 'address': address, 'emailid': emailid, 'status': status}
    new_student = models.Student(**record_to_be_added)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    student_inserted_record = new_student.to_dict()



    query = db.query(models.Student)
    query = query.filter(
        
        and_(
            models.Student.firstname < student_inserted_record,
            models.Student.age > age
        )
    )


    students = query.all()
    students = [new_data.to_dict() for new_data in students] if students else students

    res = {
        'student_inserted_record': student_inserted_record,
    }
    return res

async def post_employee(db: Session):
    res = {
    }
    return res

async def post_employee(db: Session, id: int, name: str, email: str, address: str, pincode: int):

    record_to_be_added = {'id': id, 'name': name, 'email': email, 'address': address, 'pincode': pincode}
    new_employee = models.Employee(**record_to_be_added)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    employee_inserted_record = new_employee.to_dict()



    employee_name = {}  # Creating new dict



    employee_name['shivam'] = employee_inserted_record['name']
    res = {
        'employee_dict': employee_inserted_record['name'],
    }
    return res

async def post_upload(db: Session, upload: UploadFile):

    bucket_name = "backstract-testing"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        's3',
        aws_access_key_id="AKIATET5D5CP6X5H4BNH",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1"
    )

    # Read file content
    file_content = await upload.read()

    name = upload.filename
    file_path = file_path  + '/' + name
    # Upload the file to S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_path,
        Body=file_content
    )

    # Generate the URL for the uploaded file

    file_type = Path(upload.filename).suffix
    file_size = 200
    file_url = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{file_path}"

    upload_url_file = file_url
    res = {
        'upload': upload_url_file,
    }
    return res

