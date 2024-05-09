import calendar
from datetime import datetime

import streamlit as st
#import plotly.graph_objects as go



incomes = ["Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Grocery", "Car", "Other Expenses", "Savings"]
currency = "USD"
page_title = "Income and Expense Tracker"
page_icon = ":money_with_wings:"
layout = "centered"



st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)


years =[datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])



st.header(f"Data Entry in {currency}")
with st.form("entry_form", clear_on_submit=True):
    col1,col2 = st.columns(2)
    col1.selectbox("Select Month:", months, key="months")
    col2.selectbox("Select year:", years, key="year")


    "___"

    with st.expander("Income"):
        for income in incomes:
            st.number_input(f"{income}", min_value=0, format="%i", step=10, key=income)
    with st.expander("Expenses"):
        for expense in expenses:
            st.number_input(f"{expense}", min_value=0, format="%i", step=10, key=expense)
    with st.expander("Comment"):
        comment = st.text_area("", placeholder="Enter a comment here ...")

    "___"

    submitted = st.form_submit_button("Save Data")
    if submitted:
        period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
        incomes = {income: st.session_state[income] for income in incomes}
        expenses = {expense: st.session_state[expense] for expense in expenses}
        #TODO: iNSERT VALUES INTO DATABASE

        st.write(f"incomes: {incomes}")
        st.write(f"expenses: {expenses}")
        st.write("Data saved")
    