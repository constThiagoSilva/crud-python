import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='devpy')

cursor = connection.cursor()

# cursor.execute('CREATE DATABASE devpy')

cursor.execute('CREATE TABLE users (name VARCHAR(255), age INTEGER(10))')