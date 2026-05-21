import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@MacMYSQL005",
    database="retail_oltp"
)

# create a cursor for queries
cursor = connection.cursor(dictionary=True)

