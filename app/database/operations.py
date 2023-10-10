import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup authentication with gspread
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("keyfile.json", scope)
client = gspread.authorize(creds)

# Assuming the name of your Google Sheet is 'StocksApp'
sheet = client.open("StocksApp")

def get_all_stocks():
    stocks_worksheet = sheet.worksheet("stocks")
    # Assuming first column is ID and second is name
    return stocks_worksheet.get_all_records()

def add_new_stock(name):
    stocks_worksheet = sheet.worksheet("stocks")
    # Append a new row with stock details
    next_row = len(stocks_worksheet.get_all_values()) + 1
    stocks_worksheet.append_row([next_row, name])

def record_transaction(stock_id, amount, transaction_type):
    transactions_worksheet = sheet.worksheet("transactions")
    # Append a new row with transaction details
    transactions_worksheet.append_row([stock_id, amount, transaction_type])

def get_stock_total(stock_id):
    transactions_worksheet = sheet.worksheet("transactions")
    records = transactions_worksheet.get_all_records()
    total = sum([record['amount'] for record in records if record['stock_id'] == stock_id])
    return total if total else 0
