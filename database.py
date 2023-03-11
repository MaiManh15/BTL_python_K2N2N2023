import sqlite3

connect = sqlite3.connect('DiemSinhVien_Python_K2N2_test.db')
c = connect.cursor()


c.execute('''DROP TABLE IF EXISTS "subject_student" ''')
c.execute('''DROP TABLE IF EXISTS "subject" ''')
c.execute('''DROP TABLE IF EXISTS "student" ''')
c.execute('''DROP TABLE IF EXISTS "class" ''')
c.execute('''
    CREATE TABLE IF NOT EXISTS "class" (
        classId INTEGER ,
        className varchar(10) NOT NULL,
        
        PRIMARY KEY (classId AUTOINCREMENT)
    )
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS "student" (
        studentId INTEGER ,
        studentName varchar(30) NOT NULL,
        classId int not null,

        PRIMARY KEY (studentId AUTOINCREMENT),
        FOREIGN KEY (classId) REFERENCES class(classId)
    )
''')
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
        "subjectGrade"	smallint NOT NULL,
        
        FOREIGN KEY("subjectId") REFERENCES "subject"("subjectId"),
        FOREIGN KEY("studentid") REFERENCES "student"("studentid"),
        PRIMARY KEY("subjectId","studentid")
    )
''')

connect.commit()
connect.close()
