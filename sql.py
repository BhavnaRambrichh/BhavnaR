import psycopg2 
import psycopg2.extras

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '1Direction30'
DATABASE = 'Pet Profile'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

query = "SELECT * FROM profiles"

cursor.execute(query)


results = cursor.fetchall()


connection.close()

for item in results:
    print(item)

