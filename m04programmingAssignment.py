import sqlite3

# connection string

connection = sqlite3.connect("studentDB.db")

# cursor object

cursor = connection.cursor()

# creating the tables

cursor.execute("""CREATE TABLE IF NOT EXISTS studentInfo_table(
              StudentID TEXT,
              FirstName TEXT,
              LastName TEXT,
              email TEXT,
              programID TEXT
              )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS program_table(
              programID TEXT,
              ProgramName TEXT,
              DepartmentID TEXT
              )""")
              
cursor.execute("""CREATE TABLE IF NOT EXISTS department_table(
              DepartmentID TEXT,
              DepartmentName TEXT
              )""")

# Inserting Student Data into the table via user input
print("Please enter the information of 5 students.")
x = 0
while x < 5:
    studID = input("\nStudent ID: ")
    fName = input("First Name: ")
    lName = input("Last Name:")
    email = input("Email: ")
    studProg = input("Students current program: ")
    cursor.execute("""INSERT INTO studentInfo_table(StudentID, FirstName, LastName, email, programID)
                     VALUES(?,?,?,?,?)""", (studID, fName, lName, email, studProg))
    x += 1

# Inserting program information into the table via user input
print("Please enter the information of 3 programs.")
y = 0
while y < 3:
    progID = (input("\nProgram ID: "))
    progName = input("Program Name: ")
    depID = (input("Department ID: "))
    cursor.execute("""INSERT INTO program_table(programID, ProgramName, DepartmentID)
                     VALUES(?,?,?)""", (progID, progName, depID))
    y += 1
    
# Inserting department information into the table via user input

print("Please enter the information of 1 department.")

depID = (input("\nDepartment ID: "))
depName = input("Department Name: ")

cursor.execute("""INSERT INTO department_table(DepartmentID, DepartmentName)
                     VALUES(?,?)""", (depID, depName))

# Selecting and printing data to prove that data was inserted.

cursor.execute("""SELECT * from studentInfo_table""")
print(cursor.fetchall())
cursor.execute("""SELECT * from program_table""")
print(cursor.fetchall())
cursor.execute("""SELECT * from department_table""")
print(cursor.fetchall())

connection.commit()
connection.close()