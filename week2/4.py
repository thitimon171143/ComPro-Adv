import psycopg2
from psycopg2 import Error
try:
    connection = psycopg2.connect(user="postgres",
                                    password="thitimon",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="mydb")
    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO students (student_id,f_name,l_name,e_mail) VALUES (%s,%s,%s,%s)"""
    record_to_insert = ('62060226','Thitimon','Oatthathamsunthon','6206022610076@fitm.kmutnb.ac.th')
    cursor.execute(postgres_insert_query,record_to_insert)
    '''record_to_insert = ('1','A','A','X')
    cursor.execute(postgres_insert_query,record_to_insert)
    record_to_insert = ('2','B','B','Y')
    cursor.execute(postgres_insert_query,record_to_insert)
    record_to_insert = ('3','C','C','Z')
    cursor.execute(postgres_insert_query,record_to_insert)'''
    connection.commit()
    count = cursor.rowcount
    print(count,"Record inserted successfully into students table")
except (Exception,psycopg2.Error) as error:
    if(connection):
        print("Failed to insert record into student table",error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")