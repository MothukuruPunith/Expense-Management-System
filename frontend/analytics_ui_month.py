
import pandas as pd
import streamlit as st
import requests
import altair as alt

API_URL = "https://expense-management-system11.onrender.com"

def analytics_by_month():
    response = requests.get(f"{API_URL}/analytics_month")

    if response.status_code == 200:
        data = response.json()

        # Create DataFrame
        df = pd.DataFrame(data)
        df.rename(columns={"month_year": "Month", "total_amount": "Amount"}, inplace=True)
        df["Amount"] = df["Amount"].astype(float)

        # 🔑 Create explicit Month ordering as categorical type
        df["Month"] = pd.Categorical(df["Month"], categories=df["Month"], ordered=True)

        # Create Altair bar chart
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("Month", sort=None),  # ← disables auto-sorting
            y="Amount"
        ).properties(
            title="Monthly Expenses"
        )

        st.altair_chart(chart, use_container_width=True)
        st.table(df)
    else:
        st.error("Failed to fetch analytics data.")


