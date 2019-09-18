import sqlite3

DB_FILE = 'form.db'

def create_db():
    DATABASE = sqlite3.connect(DB_FILE)
    cur=DATABASE.cursor()

    #USERS TABLE
    sql_table = """CREATE TABLE IF NOT EXISTS  users (  
                id INTEGER PRIMARY KEY,  
                name TEXT,  
                email TEXT,
                password TEXT);"""
    cur.execute(sql_table)
def insert_user(name,email,password):
    with sqlite3.connect(DB_FILE) as con:
        cur = con.cursor()
        try:
            cur.execute("Insert into users (name,email,password) values (?,?,?)",(name,email,password))
            con.commit()
            return True
        except:
            return False  