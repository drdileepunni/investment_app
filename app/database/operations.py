# operations.py

import sqlite3
from .models import DB_NAME

def get_all_stocks():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    return c.execute("SELECT id, name FROM stocks").fetchall()

def add_new_stock(name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO stocks (name) VALUES (?)", (name,))
    conn.commit()

def record_transaction(stock_id, amount, transaction_type):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO transactions (stock_id, amount, transaction_type) VALUES (?, ?, ?)", (stock_id, amount, transaction_type))
    conn.commit()

def get_stock_total(stock_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    total = c.execute("SELECT SUM(amount) FROM transactions WHERE stock_id=?", (stock_id,)).fetchone()[0]
    return total if total else 0
