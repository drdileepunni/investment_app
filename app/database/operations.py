import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import datetime
import pytz

# Setup authentication with gspread
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("keyfile.json", scope)
client = gspread.authorize(creds)

# Assuming the name of your Google Sheet is 'StocksApp'
sheet = client.open("StocksApp")

def get_all_stocks(as_pandas=False):
    stocks_worksheet = sheet.worksheet("stocks")
    if as_pandas:
        return pd.DataFrame(stocks_worksheet.get_all_records())
    # Assuming first column is ID and second is name
    return stocks_worksheet.get_all_records()

def add_new_stock(name, type):
    stocks_worksheet = sheet.worksheet("stocks")
    # Append a new row with stock details
    next_row = len(stocks_worksheet.get_all_values()) + 1
    stocks_worksheet.append_row([next_row, name, type])

    # Insert the formula in the desired column, let's say 3rd column
    price_formula = f'=GOOGLEFINANCE("{name}")'
    stocks_worksheet.update_cell(next_row, 4, price_formula)

def record_transaction(selected_stock, count, transaction_type, stock_price):
    date_str = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d")
    transactions_worksheet = sheet.worksheet("transactions")
    amount = round(count * stock_price, 1)

    # Append a new row with transaction details
    transactions_worksheet.append_row([date_str, stock_price, count, amount, selected_stock, transaction_type])

def get_stock_total(stock_name):
    transactions_worksheet = sheet.worksheet("transactions")
    records = transactions_worksheet.get_all_records()
    total = sum([record['count'] for record in records if record['stock_name'] == stock_name])
    return total if total else 0
