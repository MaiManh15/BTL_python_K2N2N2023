from fastapi import FastAPI, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Union
import numpy as np
import pandas as pd
import sql_app.models as models
import sql_app.schemas as schemas
import sql_app.data as data
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine) 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get('/')
def home():
    return "welcome BTL_Python"

@app.get('/class')
def get_class(id: Union[str, None] = None, name: Union[str, None] = None, grade: Union[int, None] = None ,db: Session = Depends(get_db)):
    
    return data.ClassroomMethod.get_class(db, id, name, grade)
@app.post('/class', response_model=schemas.ClassBase)
def create_class(classroom: schemas.ClassBase, db: Session = Depends(get_db)):
    return data.ClassroomMethod.create_class(db, classroom)