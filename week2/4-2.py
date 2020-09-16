import psycopg2
from psycopg2 import Error
try:
    connection = psycopg2.connect(user="postgres",
                                    password="thitimon",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="mydb")
    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO teachers (teacher_id,f_name,l_name,e_mail) VALUES (%s,%s,%s,%s)"""
    record_to_insert = ('AMK','K','K','KKK@gmail.com')
    cursor.execute(postgres_insert_query,record_to_insert)
    record_to_insert = ('KNM','M','M','MMM@gmail.com')
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count,"Record inserted successfully into teachers table")
except (Exception,psycopg2.Error) as error:
    if(connection):
        print("Failed to insert record into teachers table",error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")