import sqlite3

conn = sqlite3.connect('employee.db')
print("Successfully connected to the database")

conn.execute("DELETE FROM Staff where ID=4")
conn.commit()

data = conn.execute("SELECT * FROM Staff")
for rows in data:
    print("ID :", rows[0])
    print("FIRSTNAME :", rows[1])
    print("LASTNAME :", rows[2])
    print("AGE :", rows[3])
    print("SALARY :", rows[4])
    print("TASK :", rows[5])

print("Successfully removed a row")
conn.close()