import psycopg2

con = psycopg2.connect(database='northwind',
                       user='postgres',
                       password='hodi',
                       host='127.0.0.1',
                       port='5432')

print('database opened successfully')

cur = con.cursor()
cur.execute('SELECT first_name,last_name, birth_date FROM Employees')
rows = cur.fetchall() #=> [ [row]  [row] [row] [ row][row] [row]   ]

for row in rows:
    print(f'fullname - {row[0]} {row[1]} {row[2]}')
