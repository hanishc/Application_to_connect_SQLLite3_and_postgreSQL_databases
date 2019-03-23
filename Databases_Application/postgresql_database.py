import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database 1' user='postgres' password='chkhskcut' host='localhost' port='5432'")
    cur  = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT , quantity INTEGER , price REAL)")
    conn.commit()
    conn.close()

def insert_to_table(item,quantity,price):
    conn = psycopg2.connect("dbname='database 1' user='postgres' password='chkhskcut' host='localhost' port='5432'")
    cur  = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()

def update(item,quantity,price):
    conn = psycopg2.connect("dbname='database 1' user='postgres' password='chkhskcut' host='localhost' port='5432'")
    cur  = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s , price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

def delete(item):
    conn = psycopg2.connect("dbname='database 1' user='postgres' password='chkhskcut' host='localhost' port='5432'")
    cur  = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database 1' user='postgres' password='chkhskcut' host='localhost' port='5432'")
    cur  = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

create_table()
insert_to_table('Orange',5,15)
#delete('Orange')
update('Orange',10,15)
print(view())
#update('Water Glass',20,10)
#delete('Coffee Glass')
#insert_to_table('Printed Glass',15,10)
#print(view())
