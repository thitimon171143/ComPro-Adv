import psycopg2
from psycopg2 import Error
try:
    connection = psycopg2.connect(user="postgres",
                                    password="thitimon",
                                    #password="Anirach",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="mydb")
    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE Subjects
        (subjects_id     CHAR(15)    PRIMARY KEY,
        subjects_name         VARCHAR(50) NOT NULL,
        creadit        INTEGER NOT NULL,
        teacher_id         VARCHAR(3) ); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL")
except (Exception,psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL",error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")