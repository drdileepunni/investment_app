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
        amount = st.number_input("Enter amount", min_value=1)

        if st.button(action):
            if action == 'Sale':
                amount = -amount  # Convert to negative for sales
            operations.record_transaction(stock_id, amount, action)
            st.success(f"{action} recorded!")

    elif action == 'Add New Stock':
        stock_name = st.text_input("Enter new stock name")
        if st.button('Add Stock'):
            operations.add_new_stock(stock_name)
            st.success(f"Added {stock_name} to stocks!")

    elif action == 'Home Screen':
        st.subheader("Current Purchased Stocks")
        stocks = operations.get_all_stocks()
        for stock in stocks:
            total_amount = operations.get_stock_total(stock['id'])
            if total_amount > 0:  # Only show if there's some amount purchased
                st.write(f"{stock['name']}: {total_amount}")

if __name__ == "__main__":
    main()
