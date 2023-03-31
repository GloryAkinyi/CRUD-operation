import sqlite3

conn = sqlite3.connect('employee.db')
print("Connected")

conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES(1,'Andrew','Mark',21,45000.00,'Employer')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES(2,'Martha','Ann',25,54000.00,'Manager')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES(3,'Saumu','Mark',34,48000.00,'Chef')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES(4,'John','Doe',11,23000.00,'HR')")

conn.commit()
print("Successfully inserted values into Staff table")

conn.close()