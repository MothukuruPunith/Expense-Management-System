import streamlit as st
import requests
from datetime import datetime
import pandas as pd
from prompt_toolkit.shortcuts.progress_bar import Percentage

API_URL = "http://127.0.0.1:8000"
def analytics():
    col1,col2=st.columns(2)
    with col1:
        start_date = st.date_input("Start date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date":start_date.strftime("%Y-%m-%d"),
            "end_date":end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics",json=payload)
        response = response.json()
        st.write(response)
        data={
            "Category":list(response.keys()),
            "Total":[response[category]["total"] for category in response],
            "Percentage":[response[category]["percentage"] for category in response]
        }
        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage",ascending=False)
        st.bar_chart(data=df_sorted.set_index("Category")['Percentage'])
        df_sorted["Total"]=df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)
        st.table(df_sorted)

