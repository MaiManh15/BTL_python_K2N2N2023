from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./DiemSinhVien_Python_K2N2_test.db'
engine = create_engine( 
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# import sqlite3
# import numpy as np 
# import random
# import string

# connect = sqlite3.connect('DiemSinhVien_Python_K2N2.db')
# c = connect.cursor()

# c.execute('''DROP TABLE IF EXISTS "subject_student" ''')
# c.execute('''DROP TABLE IF EXISTS "subject" ''')
# c.execute('''DROP TABLE IF EXISTS "student" ''')
# c.execute('''DROP TABLE IF EXISTS "class" ''')

# startGrade = 6
# endGrade = 9
# classRoom = 6
# c.execute('''
#     CREATE TABLE IF NOT EXISTS "class" (
#         classId INTEGER ,
#         className varchar(10) NOT NULL,
#         grade smallint NOT NULL,
        
#         PRIMARY KEY (classId AUTOINCREMENT)
#     )
# ''')

# for eachGrade in range (startGrade, endGrade+1):
#     for eachClass in range (1, classRoom+1):
#         c.execute('''INSERT INTO "class"("className","grade") VALUES (?, ?)''', [f'{eachGrade}A{eachClass}', f'{eachGrade}'])
 
# c.execute('''
#     CREATE TABLE IF NOT EXISTS "student" (
#         studentId INTEGER ,
#         studentName varchar(50) NOT NULL,
#         classId INTEGER not null,

#         PRIMARY KEY (studentId AUTOINCREMENT),
#         FOREIGN KEY (classId) REFERENCES class(classId)
#     )
# ''')

# studentEachClass = 30
# studentSum = classRoom * studentEachClass
# middleNameList = ["Hoàng", "Văn", "Quang", "Quốc", "Thị", "Minh"]
# firstNameList = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương" ,"Lý"]

# def classIsReady(classId, studentEachClass, classRoom):
#     studentInClass = c.execute('''SELECT * FROM "student" WHERE classId == ?''', [classId])
    
#     if(len(studentInClass.fetchall()) < studentEachClass):
#         return classId
#     else:
#         classIdNew = int(np.ceil(classRoom*np.random.random()))
#         studentEachClassNew = studentEachClass
#         classRoomNew = classRoom
#         return classIsReady(classIdNew, studentEachClassNew, classRoomNew)
# def setStudentToClass(classId):
#     firstName = firstNameList[int(np.floor(len(firstNameList) * np.random.random()))]
#     middleName =  middleNameList[int(np.floor(len(middleNameList) * np.random.random()))]
#     lastName = random.choices(string.ascii_uppercase, k=1)
#     c.execute('''INSERT INTO "student"("studentName", "classId") VALUES (? ,?)''', [f'{firstName} {middleName} {lastName[0]}', classId])

# for eachstudent in range (0, studentSum):
#     classId = int(np.ceil(classRoom *np.random.random()))
#     setStudentToClass(classIsReady(classId, studentEachClass, classRoom))

# c.execute('''
#     CREATE TABLE IF NOT EXISTS "subject" (
#         subjectId INTEGER , 
#         subjectName varchar(20) NOT NULL, 
        
#         PRIMARY KEY (subjectId AUTOINCREMENT)
#     )
# ''')
# listSubject = [
#     ["Toán"],
#     ["Văn"],
#     ["Tiếng Anh"],
#     ["Vật lý"],
#     ["Hóa học"],
#     ["Sinh học"],
#     ["Lịch sử"],
#     ["Địa lý"],
#     ["Giáo dục công dân"],
#     ["Thể dục"]
# ]
# c.executemany('''INSERT INTO "subject"("subjectName") VALUES (?)''', listSubject)

# c.execute('''
#     CREATE TABLE IF NOT EXISTS "subject_student" (
#         "subjectId"	INTEGER NOT NULL,
#         "studentid"	INTEGER NOT NULL,
#         "subjectPoint"	REAL NOT NULL,
        
#         FOREIGN KEY("subjectId") REFERENCES "subject"("subjectId"),
#         FOREIGN KEY("studentid") REFERENCES "student"("studentid"),
#         PRIMARY KEY("subjectId","studentid")
#     )
# ''')
# for student in range(0, studentSum):
#     subjectLen = c.execute('''SELECT * FROM "subject" ''')
#     for subject in range(0, len(subjectLen.fetchall())):
#         c.execute('''INSERT INTO "subject_student" VALUES (?,?,?) ''', [ subject +1 , student+1 , np.round(np.random.random()*10 , 2)])
    
    
# connect.commit()
# connect.close()