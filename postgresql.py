import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database 1' user='postgres' password='chkhskcut' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

create_table()

def insert(item,quantity,price):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

insert("Wine Glass",10,5.5)
insert("Coffee Cups",10,5)
insert("Water Glass",80,9.5)

def delete(item):
    print(item)
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()


delete("Wine glass")

def update(quantity,price,item):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item))
    conn.close()
    conn.close()

update(11,6,"Water Glass")
def view():
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
#   Rows is returned as a Python List.
    return rows

print(view())
