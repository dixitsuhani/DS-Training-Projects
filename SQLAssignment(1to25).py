import mysql.connector
conn= mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "Dixit_3004"
)
cursor= conn.cursor()
# cursor.execute("CREATE DATABASE College")
cursor.execute("USE College")

# cursor.execute("""
#     CREATE TABLE Students(
#         S_Id INT PRIMARY KEY,
#         Name VARCHAR(60),
#         Age INT,
#         Gender ENUM('F', 'M', 'O'),
#         Department VARCHAR(100)
#         )
# """)

# students_data= [
#     (101, "Vivek", 21, 'M', "Computer Science"),
#     (102, "Suresh", 23, 'M', "Electrical"),
#     (103, "Akshay", 21, 'M', "Computer Science"),
#     (104, "Raveena", 19, 'F', "Software Engineering"),
#     (105, "Shilpa", 20, 'F', "Media and Information")
# ]
# cursor.executemany("INSERT INTO Students (S_Id, Name, Age, Gender, Department) VALUES (%s, %s, %s, %s, %s)", students_data)
# conn.commit()

# cursor.execute("SELECT * FROM Students")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM Students WHERE Age>20")
# print(cursor.fetchall())

# cursor.execute("UPDATE Students SET Department= 'Mechanical' WHERE Name= 'Suresh'")
# conn.commit()

# cursor.execute("DELETE FROM Students WHERE S_Id= 103")
# conn.commit()

# cursor.execute("SELECT * FROM Students ORDER BY Age DESC")
# print(cursor.fetchall())

# cursor.execute("SELECT DISTINCT Department FROM Students")
# print(cursor.fetchall())

# cursor.execute("SELECT COUNT(*) FROM Students")
# print(cursor.fetchone())

# cursor.execute("RENAME TABLE Students TO Students_Info")

# cursor.execute("ALTER TABLE Students_Info ADD Email VARCHAR(100)")

# cursor.execute("SELECT * FROM Students_Info WHERE Name LIKE 'A%'")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM Students_Info WHERE Age BETWEEN 18 AND 25")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM Students_Info ORDER BY Age DESC LIMIT 1")
# print(cursor.fetchone())

# cursor.execute("SELECT * FROM Students_Info LIMIT 3")
# print(cursor.fetchall())

# cursor.execute("""
#     CREATE TABLE Courses(
#         C_Id INT PRIMARY KEY,
#         C_Name VARCHAR(100),
#         Credits INT       
#         )
# """)

# courses_data= [
#     (201, "BCA", 12),
#     (202, "BBA", 12),
#     (203, "BAJMC", 15)
# ]
# cursor.executemany("INSERT INTO Courses (C_Id, C_Name, Credits) VALUES (%s, %s, %s)", courses_data)
# conn.commit()

# cursor.execute("SELECT * FROM Students_Info WHERE Department= 'Computer Science'")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM Students_Info WHERE Department IN ('Computer Science', 'Electrical')")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM Students_Info WHERE Age BETWEEN 20 AND 30")
# print(cursor.fetchall())

# cursor.execute("SELECT NOW()")
# print(cursor.fetchone())

# cursor.execute("SELECT Name AS S_Name, Age FROM Students_Info")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM Students_Info WHERE Department!= 'Mechanical'")
# print(cursor.fetchall())

# cursor.execute("DELETE FROM Students_Info")
# conn.commit()

cursor.close()
conn.close()