import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

dataBase = mysql.connector.connect(
    user='root',
	password=os.getenv('MYSQL_PASSWORD'),
	host='localhost'
)

cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE blog_db")

print("Database created successfully")