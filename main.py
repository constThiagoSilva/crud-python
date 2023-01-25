import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', passwd='root', database='devpy')

cursor = db.cursor()

# cursor.execute('CREATE DATABASE devpy')

# cursor.execute('CREATE TABLE users (name VARCHAR(255), age INTEGER(10))')

# sql_insert_command = 'INSERT INTO users (name, age) VALUES (%s, %s)'
# user = ('Thiago', 17)

# cursor.execute(sql_insert_command, user)

# sql_insert_command = 'INSERT INTO users (name, age) VALUES (%s, %s)'
# users = [('Maria', 20), ('João', 24), ('Pedro', 62)]

# cursor.executemany(sql_insert_command, users)

# db.commit()

cursor.execute('SELECT * FROM users')

users = cursor.fetchall()

for user in users:
    print(user)