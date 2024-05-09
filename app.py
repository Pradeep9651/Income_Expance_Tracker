import streamlit as st
import plotly.graph_objects as go



incomes = ["Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Grocery", "Car", "Other Expenses", "Savings"]
currency = "USD"
page_title = "Income and Expense Tracker"
page_icon = ":money_with_wings:"
layout = "centered"



st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)