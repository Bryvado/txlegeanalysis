import sqlite3

def create_db(db_path='txlege.db'):
    """
    Create a SQLite database to store Texas Legislature data.
    
    :param db_path: Path to the database file
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create a table for bills
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bills (
        bill_number TEXT,
        chamber TEXT,
        status TEXT,
        file_path TEXT
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
    print("Database created successfully.")
