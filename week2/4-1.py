import psycopg2
from psycopg2 import Error
try:
    connection = psycopg2.connect(user="postgres",
                                    password="thitimon",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="mydb")
    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO subjects (subjects_id,subjects_name,creadit,teacher_id) VALUES (%s,%s,%s,%s)"""
    record_to_insert = ('060233205','Adv-Network','3','KNM')
    cursor.execute(postgres_insert_query,record_to_insert)
    record_to_insert = ('060233113','Adv-ComPro','3','AMK')
    cursor.execute(postgres_insert_query,record_to_insert)
    record_to_insert = ('080103034','English Conver','3','SPK')
    cursor.execute(postgres_insert_query,record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count,"Record inserted successfully into subjects table")
except (Exception,psycopg2.Error) as error:
    if(connection):
        print("Failed to insert record into subjects table",error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")