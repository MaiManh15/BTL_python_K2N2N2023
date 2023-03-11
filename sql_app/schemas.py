from typing import Union
from pydantic import BaseModel

class ClassBase(BaseModel):
    className: Union[str, None] = None
    classGrade: Union[str, None] = None
    
class ClassCreate(ClassBase):
    pass
    
class SubjectBase(BaseModel):
    subjectName: str
    
class SubjectCreate(SubjectBase):
    pass

class StudentBase(BaseModel):
    studentName: str
    classIn : int

class StudentCreate(StudentBase):
    pass

class SubjectStudentPointBase(BaseModel):
    studentId: int
    subjectId: int

class SubjectStudentPointCreate(SubjectStudentPointBase):
    point: float
    class Config:
        orm_mode = True
    
class ClassStudent(ClassBase):
    id: int
    class Config:
        orm_mode = True

class Suject(SubjectBase):
    id: int
    class Config:
        orm_mode = True    
    
class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True

class SubjectStudentPoint():
    class Config:
        orm_mode = True
        