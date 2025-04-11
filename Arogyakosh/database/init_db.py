from connection import connect

def init():
    with connect() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            condition TEXT
        )""")
        # Add other tables similarly
