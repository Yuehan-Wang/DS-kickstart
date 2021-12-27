import streamlit as st
import pandas as pd
import numpy as np
import requests

st.sidebar.title("Stock")
op = st.sidebar.selectbox(
    "Which Dashboard?",
    ("Twitter","Google","Pick Your Own Stock"),
    2)

st.header(op+" Daily Open/Close")

if op == "Google":
    r = requests.get("https://api.polygon.io/v1/open-close/GOOGL/2021-12-20?adjusted=true&apiKey=2RsZzwKc4SWPGLSY861uPBABHgbF0kpa")
    data = r.json()
    st.write(data)
    st.image("https://finviz.com/chart.ashx?t=GOOGL")
if op == "Twitter":
    r = requests.get("https://api.polygon.io/v1/open-close/TW/2021-12-20?adjusted=true&apiKey=2RsZzwKc4SWPGLSY861uPBABHgbF0kpa")
    data = r.json()
    st.write(data)
    st.image("https://finviz.com/chart.ashx?t=TW")
if op == "Pick Your Own Stock":
    symbol = st.sidebar.text_input("Stock Symbol", value='AAPL',max_chars=10)
    r = requests.get(f"https://api.polygon.io/v1/open-close/{symbol}/2021-12-20?adjusted=true&apiKey=2RsZzwKc4SWPGLSY861uPBABHgbF0kpa")
    data = r.json()
    st.write(data)
    st.image(f"https://finviz.com/chart.ashx?t={symbol}")
 


