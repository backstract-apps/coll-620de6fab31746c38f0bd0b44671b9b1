from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/student/')
async def get_student(db: Session = Depends(get_db)):
    try:
        return await service.get_student(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/student/id')
async def get_student_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_student_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/student/')
async def post_student(id: int, firstname: str, lastname: str, age: int, address: str, emailid: str, status: int, db: Session = Depends(get_db)):
    try:
        return await service.post_student(db, id, firstname, lastname, age, address, emailid, status)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/student/id/')
async def put_student_id(raw_data: schemas.PutStudentId, db: Session = Depends(get_db)):
    try:
        return await service.put_student_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/student/id')
async def delete_student_id(id: str, firstname: str, lastname: str, age: str, address: str, emailid: str, status: str, db: Session = Depends(get_db)):
    try:
        return await service.delete_student_id(db, id, firstname, lastname, age, address, emailid, status)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/employee')
async def post_employee(db: Session = Depends(get_db)):
    try:
        return await service.post_employee(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/employee')
async def post_employee(id: int, name: str, email: str, address: str, pincode: int, db: Session = Depends(get_db)):
    try:
        return await service.post_employee(db, id, name, email, address, pincode)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/upload')
async def post_upload(upload: UploadFile, db: Session = Depends(get_db)):
    try:
        return await service.post_upload(db, upload)
    except Exception as e:
        raise HTTPException(500, str(e))

