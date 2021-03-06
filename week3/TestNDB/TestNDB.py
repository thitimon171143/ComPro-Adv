import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                    password="OEIknz76159",
                                    host="node1438-thitimon.app.ruk-com.cloud",
                                    port="11023",
                                    database="postgres")
    connection.autocommit = True
    cursor = connection.cursor()
    sql = '''CREATE database TestDB'''
    cursor.execute(sql)
    print("Database created successfully.........")
except (Exception,psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL",error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")