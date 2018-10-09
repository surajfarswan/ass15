## DATABASE USING PYTHON

# Question 1

import sqlite3
try:
    con = sqlite3.connect('Student.db')
    cursor = con.cursor()
    query = "create table student(name varchar(10), marks int(3))"
    cursor.execute(query)
    print('Table created successfully')
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!!')
print()

# Quetion 2

record = []
for i in range(10):
    record.append((input('Enter name: '),int(input('Enter marks: '))))
print()

# Question 3

try:
    con = sqlite3.connect('Student.db')
    cursor = con.cursor()
    query = "insert into Student(name,marks) values(?,?)"
    cursor.executemany(query,record)
    con.commit()
    print('Query commited')
    q = 'select * from Student'
    cursor.execute(q)
    data = cursor.fetchall()
    for row in data:
        print("Name: {}, Marks: {}".format(row[0],row[1]))
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!!')
print()

# Question 4

try:
    con = sqlite3.connect('Student.db')
    cursor = con.cursor()
    query = "select * from Student where marks >80"
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print('Name: {}, Marks: {}'.format(row[0],row[1]))
except sqlite3.DatabaeError as e:
    if con:
        con.rollback()
        print('Problem occured: ',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!!')
print()
