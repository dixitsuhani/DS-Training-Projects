import mysql.connector
conn= mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "Dixit_3004"
)
cursor= conn.cursor()

cursor.execute("USE College")

# cursor.execute("""
#     CREATE TABLE Marks(
#         S_Id INT,
#         Subject VARCHAR(100),
#         Marks INT,
#         FOREIGN KEY (S_Id) REFERENCES Students_Info(S_Id)
#         )
# """)

# marks_data= [
#     (101, 'DBMS', 90),
#     (101, 'DSA', 85),
#     (102, 'DBMS', 78),
#     (102, 'DSA', 84),
#     (103, 'DBMS', 87),
#     (103, 'DSA', 89),
#     (104, 'DBMS', 75),
#     (104, 'DSA', 80),
#     (105, 'DBMS', 76),
#     (105, 'DSA', 88)
# ]
# cursor.executemany("INSERT INTO Marks (S_Id, Subject, Marks) VALUES (%s, %s, %s)", marks_data)
# conn.commit()

# cursor.execute("""
#     SELECT s.S_Id, s.Name, m.Subject, m.Marks
#     FROM Students_Info s
#     JOIN Marks m ON s.S_Id = m.S_Id
# """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT S_Id, AVG(Marks) AS Average_Marks
#     FROM Marks
#     GROUP BY S_Id
# """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT S_Id, SUM(Marks) AS Total_Marks 
#     FROM Marks 
#     GROUP BY S_Id
# """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT S_Id, SUM(Marks) as Total
#     FROM Marks
#     GROUP BY S_Id
#     HAVING Total>200
# """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT Age, COUNT(*) AS Count
#     FROM Students_Info
#     GROUP BY Age
#     HAVING Count>1
# """)
# print(cursor.fetchall())

# INNER JOIN: Returns all the matching records on the basis of one common column
# cursor.execute("""
#     SELECT s.Name, m.Subject, m.Marks
#     FROM Students_Info s 
#     INNER JOIN Marks m ON s.S_Id=m.S_Id
# """)
# print("Inner Join: ", cursor.fetchall())

# LEFT JOIN: Returns all columns from the left table (Students_Info) but only matching columns from the right table (Marks)
# cursor.execute("""
#     SELECT s.Name, m.Subject, m.Marks
#     FROM Students_Info s
#     LEFT JOIN Marks m ON s.S_Id=m.S_Id
# """)
# print("Left Join: ", cursor.fetchall())

# RIGHT JOIN: Returns all columns from the right table (Marks) but only the matching columns from the left table (Students_Info)
# cursor.execute("""
#     SELECT s.Name, m.Subject, m.Marks
#     FROM Students_Info s
#     RIGHT JOIN Marks m ON s.S_Id=m.S_Id
# """)
# print("Right Join: ", cursor.fetchall())

# cursor.execute("""
#     CREATE TABLE Library(
#         Book_Id INT AUTO_INCREMENT PRIMARY KEY,
#         Title VARCHAR(100)
#         )
# """)

# cursor.execute("""
#     CREATE TABLE Enrollments(
#         Enrollment_No INT AUTO_INCREMENT PRIMARY KEY,
#         S_Id INT,
#         C_Id INT,
#         FOREIGN KEY (S_Id) REFERENCES Students_Info(S_Id),
#         FOREIGN KEY (C_Id) REFERENCES Courses
#         )
# """)

# cursor.execute("SELECT MAX(Marks) FROM Marks")
# print(cursor.fetchone())

# cursor.execute("""
#     CREATE VIEW Student_Total_Marks AS
#     SELECT s.Name, SUM(m.Marks) AS Total_Marks
#     FROM Students_Info s
#     JOIN Marks m ON s.S_Id=m.S_Id
#     GROUP BY s.Name
# """)

# cursor.execute("""
#     SELECT S_Id, SUM(Marks) AS Total
#     FROM Marks
#     GROUP BY S_Id
#     HAVING Total> (SELECT AVG(Marks) * COUNT(DISTINCT Subject) FROM Marks)
# """)
# print(cursor.fetchall())

# cursor.execute("""
#     CREATE PROCEDURE insert_student(IN SId INT, IN SName VARCHAR(60), IN SAge INT, IN SGender CHAR(1), IN SDept VARCHAR(100))
#     BEGIN
#                INSERT INTO Students_Info(S_Id, Name, Age, Gender, Department)
#                VALUES(SId, SName, SAge, SGender, SDept);
#     END
# """)
# cursor.execute("CALL insert_student(106, 'Ravi', 22, 'M', 'Civil')")
# conn.commit()

# cursor.execute("""
#     CREATE PROCEDURE update_dept(IN SId INT, IN NewDept VARCHAR(100))
#     BEGIN
#                UPDATE Students_Info SET Department= NewDept WHERE S_Id= SId;
#     END
# """)
# cursor.execute("CALL update_dept(106, 'Mechanical')")
# conn.commit()

# cursor.execute("""
#     CREATE FUNCTION calculate_grade(Marks INT) RETURNS VARCHAR(10)
#     DETERMINISTIC
#     RETURN
#             CASE
#                 WHEN Marks>= 90 THEN 'A'
#                 WHEN Marks>= 80 THEN 'B'
#                 WHEN Marks>= 70 THEN 'C'
#                 ELSE 'D'
#             END
# """)
# cursor.execute("SELECT calculate_grade(87)")
# print(cursor.fetchone())

# cursor.execute("""
#     CREATE TABLE Student_Log(
#         Log_Id INT AUTO_INCREMENT PRIMARY KEY,
#         S_Id INT,
#         Action_Time DATETIME       
#         )
# """)
# cursor.execute("""
#     CREATE TRIGGER log_insert
#     AFTER INSERT ON Students_Info
#     FOR EACH ROW
#     INSERT INTO Student_Log(S_Id, Action_Time)
#     VALUES(NEW.S_Id, NOW())
# """)

# try:
#     conn.start_transaction()
#     cursor.execute("UPDATE Students_Info SET Age= Age+1 WHERE S_Id= 101")
#     cursor.execute("UPDATE Students_Info SET Age= Age+1 WHERE S_Id= 102")
#     conn.commit()
# except:
#     conn.rollback()

# cursor.execute("""
#     SELECT Name, COUNT(*) FROM Students_Info
#     GROUP BY Name
#     HAVING COUNT(*) > 1
# """)
# print(cursor.fetchall())

# cursor.execute("""
#     CREATE TABLE csv_data(
#         id INT,
#         name VARCHAR(100),
#         score INT       
#         )
# """)

# cursor.execute("CREATE INDEX Information ON Students_Info(Name)")

# cursor.execute("""
#     SELECT MAX(Marks) FROM Marks
#     WHERE Marks < (SELECT MAX(Marks) FROM Marks)
# """)
# print(cursor.fetchone())

# cursor.execute("DROP TABLE Enrollments")
# cursor.execute("DROP TABLE Courses")
# conn.commit()

# cursor.close()
# conn.close()