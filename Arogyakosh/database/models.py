from connection import connect

def get_all_patients():
    with connect() as conn:
        return conn.execute("SELECT * FROM patients").fetchall()
