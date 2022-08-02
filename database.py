import mysql.connector as sql
import pandas as pd
from mysql.connector import Error
connection = sql.connect(
    user="root", password="1234", host="127.0.0.1",database="test_database"
)

try: 
    if connection.is_connected():
        cursor = connection.cursor()
        data = pd.read_csv("./data/users.csv")
        df = pd.DataFrame(data=data,columns=["first_name","last_name","dob","email","city"])

        for index in df.index:
            firstName = df["first_name"][index]
            last_name = df["last_name"][index]
            dob = df["dob"][index]
            email = df["email"][index]
            city = df["city"][index]
            query = f"""
            insert into customers (first_name,last_name,dob,email,city) values("{firstName}","{last_name}","{dob}","{email}","{city}");
            """
            cursor.execute(query)
            connection.commit()


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        connection.close()
        # cursor.close()
