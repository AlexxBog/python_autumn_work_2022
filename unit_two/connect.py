import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="auth",
    user="postgres",
    password="4832")
print(conn)
cur = conn.cursor()
id_student = int(input("Введите имя студента:"))
SQL_GET_TASK_BY_STUDENT = f"""

SELECT * 
FROM publiv.accaunts
WHERE id = {id_student}

"""


cur.execute(SQL_GET_TASK_BY_STUDENT)
records = cur.fetchall()
for row in records:
    print(row)

conn.close()

print(conn)