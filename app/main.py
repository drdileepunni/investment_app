# main.py

import streamlit as st
from database import operations

def main():
    # Title
    st.title('Multi-Stock Tracker!')

    # Sidebar for actions
    st.sidebar.title('Actions')
    action = st.sidebar.selectbox("Choose an action", ['Home Screen', 'Purchase', 'Sale', 'Add New Stock'])

    if action == 'Purchase' or action == 'Sale':
        stocks = operations.get_all_stocks()
        stock_names = [s['name'] for s in stocks]
        selected_stock = st.selectbox("Choose a stock", stock_names)
        stock_id = [s['id'] for s in stocks if s['name'] == selected_stock][0]
        stock_price = [s['price'] for s in stocks if s['name'] == selected_stock][0]
        count = st.number_input("Enter count", min_value=1)

        if st.button(action):
            if action == 'Sale':
                count = -count  # Convert to negative for sales
            operations.record_transaction(selected_stock, count, action, stock_price)
            st.success(f"{action} recorded!")

    elif action == 'Add New Stock':
        stock_name = st.text_input("Enter new stock name")
        stock_type = st.selectbox("Enter new stock name", ["Company", "ETF"])
        if st.button('Add Stock'):
            operations.add_new_stock(stock_name, stock_type)
            st.success(f"Added {stock_name} to stocks!")

    elif action == 'Home Screen':
        st.subheader("Current Purchased Stocks")
        stocks = operations.get_all_stocks()
        for stock in stocks:
            total_count = operations.get_stock_total(stock['name'])
            if total_count > 0:  # Only show if there's some count purchased
                st.write(f"{stock['name']}: {total_count}")

if __name__ == "__main__":
    main()
