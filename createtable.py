import sqlite3

conn = sqlite3.connect('employee.db')
print("Connected successfully")

conn.execute("""CREATE TABLE Staff(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
AGE INT,
SALARY REAL,
TASK TEXT CHAR(50))""")

print("Successfully created Staff table")
conn.close()