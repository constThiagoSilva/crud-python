import mysql.connector
from mysql.connector import errorcode
from .config.database_config import config

try:
    connection = mysql.connector.connect(**config)
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(error)

