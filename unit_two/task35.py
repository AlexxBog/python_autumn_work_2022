# todo:
#1. Скачать http-clent https://insomnia.rest/download
#2. Создать новый проект и установить flask,
#3. Создать файл requirements.txt  в который занести устанавливаемые библиотеки
#4. Написать роутеры для REST сервиса/

import psycopg2
from flask import Flask
import json

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='task',
                            user='postgres',
                            password='4511')
    return conn


@app.route('/student/{id}', methods=['GET'])
def get(self, id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name FROM students_task where students_id = 1')
    name = cur.fetchall()
    return name


# """ Передаем изменения в json """
# router /student/{id}
# def post(self, id):
#      return jsonify(id)

# """ Добавить студента в json """
# @app.route( /student/
#     def put(self, id):


# """ Удалим студента по {id}"""
# router /student/{id}
# def delete(self):


# 5. Реализовать роутер /student/list - получение списка всех студентов
# студенты могут храниться как в коллекции так и в БД

@app.route('/student/list')
def get(self):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name FROM students_task')
    name = cur.fetchall()
    for row in name:
        return name


if __name__ == "__main__":
    app.run()

cur.close()
conn.close()





