# models.py

import sqlite3

DB_NAME = "/Users/drdileepunni/github_/investment_app//data/stocks_db.sqlite"

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Create stocks table
    c.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')

    # Create transactions table
    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            stock_id INTEGER,
            amount INTEGER NOT NULL,
            transaction_type TEXT NOT NULL,
            FOREIGN KEY (stock_id) REFERENCES stocks (id)
        )
    ''')

    conn.commit()
    conn.close()

# Call this function when the app starts or module is imported to ensure tables are created.
create_tables()
