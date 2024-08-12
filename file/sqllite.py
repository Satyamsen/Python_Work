import sqlite3

def connect_db():
    conn = sqlite3.connect("Ram.db")
    cur = conn.cursor()
    return conn, cur


def create_table():
    conn, cur = connect_db()
    cur.execute('''CREATE TABLE IF NOT EXISTS Ram (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    dob TEXT NOT NULL)''')
    conn.commit()
    conn.close()


def load_data():
    conn, cur = connect_db()
    cur.execute("SELECT * FROM Ram")
    rows = cur.fetchall()
    conn.close()
    return rows


def add_person(name, age, dob):
    conn, cur = connect_db()
    cur.execute("INSERT INTO Ram (name, age, dob) VALUES (?, ?, ?)", (name, age, dob))
    conn.commit()
    conn.close()

def update_person(id, new_name, new_age, new_dob):
    conn, cur = connect_db()
    cur.execute("UPDATE Ram SET name = ?, age = ?, dob = ? WHERE id = ?", (new_name, new_age, new_dob, id))
    conn.commit()
    conn.close()
