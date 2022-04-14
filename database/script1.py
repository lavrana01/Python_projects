import psycopg2


def create_table():

        conn = psycopg2.connect("dbname='postgres' user='postgres' password='LavRana2810' host='localhost' port='5432'")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
        cur.execute("INSERT INTO store VALUES ('wine glass',10,10.5)")
        conn.commit()
        conn.close()

def insert(item,quantity,price):
    
        conn = psycopg2.connect("dbname='postgres' user='postgres' password='LavRana2810' host='localhost' port='5432'")
        cur = conn.cursor()
        cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
        conn.commit()
        conn.close()

#insert("Orange",10,8)

def view():
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='LavRana2810' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows




def delete(item):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='LavRana2810' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()
    
#delete("wine glass")

def update(quantity,price,item):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='LavRana2810' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

#create_table()
#update(10,20,'Orange')
#print(view())
