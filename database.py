import sqlite3
import numpy as np 
import random
import string

connect = sqlite3.connect('DiemSinhVien_Python_K2N2_test.db')
c = connect.cursor()


c.execute('''DROP TABLE IF EXISTS "subject_student" ''')
c.execute('''DROP TABLE IF EXISTS "subject" ''')
c.execute('''DROP TABLE IF EXISTS "student" ''')
c.execute('''DROP TABLE IF EXISTS "class" ''')

classRoom = 6
startGrade = 10
endGrade = 12
listClass  = []
for eachGrade in range (startGrade, endGrade+1):
    for eachClass in range (1, classRoom+1):
        listClass.append([f'{eachGrade}A{eachClass}', f'{eachGrade}'])
    
c.execute('''
    CREATE TABLE IF NOT EXISTS "class" (
        classId INTEGER ,
        className varchar(10) NOT NULL,
        grade smallint NOT NULL,
        
        PRIMARY KEY (classId AUTOINCREMENT)
    )
''')

c.executemany('''INSERT INTO "class"("className","grade") VALUES (?, ?)''', listClass)


student = 20
listStudent = []
listStudentLeftClass = []
studentEachClass = 30
for classNum in range(0, classRoom):
    listStudentLeftClass.append(30)
    

def classIsReadyForStudent(studentLeftArray, classRoom):
    classGetIn = int(np.floor(classRoom * np.round(np.random.random(), 2)) )
    if(studentLeftArray[classGetIn] == 0):
        allFull = True
        for classNum in studentLeftArray:
            if(studentLeftArray[classNum] != 0):
                allFull = False
        if(allFull == False):
            classIsReadyForStudent(studentLeftArray, classRoom)
        else: 
            return 0
    else:
        return classGetIn    

middleNameList = ["Hoàng", "Văn", "Quang", "Quốc", "Thị", "Minh"]
firstNameList = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương" ,"Lý"]

for eachstudent in range (0, student):
    roomReady = classIsReadyForStudent(listStudentLeftClass, classRoom)
    if(roomReady !=0):
        listStudentLeftClass[roomReady] = listStudentLeftClass[roomReady] -1;
        firstName = firstNameList[int(np.floor(len(firstNameList) * np.random.random()))]
        middleName =  middleNameList[int(np.floor(len(middleNameList) * np.random.random()))]
        lastName = random.choices(string.ascii_uppercase, k=1)
        listStudent.append([f'{firstName} {middleName} {lastName[0]}', roomReady])
        
c.execute('''
    CREATE TABLE IF NOT EXISTS "student" (
        studentId INTEGER ,
        studentName varchar(50) NOT NULL,
        classId int not null,

        PRIMARY KEY (studentId AUTOINCREMENT),
        FOREIGN KEY (classId) REFERENCES class(classId)
    )
''')

c.executemany('''INSERT INTO "student"("studentName","classId") VALUES (?, ?)''', listStudent)
c.execute('''
    CREATE TABLE IF NOT EXISTS "subject" (
        subjectId INTEGER , 
        subjectName varchar(20) NOT NULL, 
        
        PRIMARY KEY (subjectId AUTOINCREMENT)
    )
''')
listSubject = [
    ["Toán"],
    ["Văn"],
    ["Tiếng Anh"],
    ["Vật lý"],
    ["Hóa học"],
    ["Sinh học"],
    ["Lịch sử"],
    ["Địa lý"],
    ["Giáo dục công dân"],
    ["Thể dục"]
]
c.executemany('''INSERT INTO "subject"("subjectName") VALUES (?)''', listSubject)
c.execute('''
    CREATE TABLE IF NOT EXISTS "subject_student" (
        "subjectId"	int NOT NULL,
        "studentid"	int NOT NULL,
        "subjectPoint"	smallint NOT NULL,
        
        FOREIGN KEY("subjectId") REFERENCES "subject"("subjectId"),
        FOREIGN KEY("studentid") REFERENCES "student"("studentid"),
        PRIMARY KEY("subjectId","studentid")
    )
''')

connect.commit()
connect.close()
