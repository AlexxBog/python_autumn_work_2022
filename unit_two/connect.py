import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="auth",
    user="postgres",
    password="4832")
print(conn)

#Пишем первый запрос
cur = conn.cursor()
new = """ 

SELECT *
FROM project.client

"""

cur.execute(new)
records = cur.fetchall()
for row in records:
    print(row)



#Пишем второй запрос

cur = conn.cursor()
new = """ 

SELECT *
FROM project.company

"""

cur.execute(new)
records = cur.fetchall()
for row in records:
    print(row)






conn.close()