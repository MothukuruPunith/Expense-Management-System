import streamlit as st
# import pandas as pd
import requests
# from datetime import datetime
from add_update import add_update
from analytics_ui_date import analytics
from analytics_ui_month import analytics_by_month
API_URL = "https://expense-management-system11.onrender.com"
st.title("EXPENSE MANAGEMENT SYSTEM")
tab1,tab2,tab3 = st.tabs(["Add/Update","Analytics by Date","Analytics by Month"])
with tab1:
    add_update()
with tab2:
    analytics()
with tab3:

    analytics_by_month()

