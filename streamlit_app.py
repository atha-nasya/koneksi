# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import numpy as np

url = "https://docs.google.com/spreadsheets/d/1BtV9yJv4YosVkH48ZTXkXBeX2knpaS8Mu6QfOP59heo/edit?gid=0#gid=0"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)