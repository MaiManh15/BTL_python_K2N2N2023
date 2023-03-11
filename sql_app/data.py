
from sqlalchemy.orm import Session
from typing import Union
import sql_app.models as models
import sql_app.schemas as schemas

class ClassroomMethod:
    def create_class(db:Session, classroom: schemas.ClassBase):
        db_classroom = models.Classroom(name = classroom.className, grade = classroom.classGrade)
        db.add(db_classroom)
        db.commit()
        db.refresh(db_classroom)
        return db_classroom
    
    def get_class(db:Session, id: Union[str, None] = None, name: Union[str, None] = None, grade: Union[int, None] = None ):
        return db.query(models.Classroom).filter(models.Classroom.id == id, models.Classroom.name == name, models.Classroom.grade == grade).all()
    
    def get_all(db:Session):
        return db.query(models.Classroom).all()
