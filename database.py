import sqlite3

connect = sqlite3.connect('DiemSinhVien_Python_K2N2.db')
c = connect.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS "class" (
        classId INTEGER  ,
        className varchar(10) NOT NULL,
        
        PRIMARY KEY (classId)
    )
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS "student" (
        studentId INTEGER  ,
        studentName varchar(30) NOT NULL,
        classId int not null,

        PRIMARY KEY (studentId),
        FOREIGN KEY (classId) REFERENCES class(classId)
    )
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS "subject" (
        subjectId INTEGER , 
        subjectName varchar(20) NOT NULL, 
        PRIMARY KEY (subjectId)
    )
''')
listSubject = [
    (1,"Toán"),
    (2,"Văn"),
    (3,"Tiếng Anh"),
    (4,"Vật lý"),
    (5,"Hóa học"),
    (6,"Sinh học"),
    (7,"Lịch sử"),
    (8,"Địa lý"),
    (9,"Giáo dục công dân"),
    (10,"Thể dục")
]
# c.executemany('''INSERT INTO "subject" VALUES (?, ?)''', listSubject)
c.execute('''
    CREATE TABLE IF NOT EXISTS "subject_student" (
        "subjectId"	int NOT NULL,
        "studentid"	int NOT NULL,
        "subjectGrade"	smallint NOT NULL,
        FOREIGN KEY("subjectId") REFERENCES "subject"("subjectId"),
        UNIQUE("studentId"),
        PRIMARY KEY("subjectId","studentid")
    )
''')

connect.commit()
connect.close()
