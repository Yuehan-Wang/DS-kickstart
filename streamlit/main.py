import streamlit as st
import pandas as pd
import numpy as np
import requests

st.sidebar.title("options")
op = st.sidebar.selectbox(
    "Which Dashboard?",
    ("twitter","google","real estate"))

st.header(op)



if op == "google":
    r = requests.get("https://api.polygon.io/v2/aggs/ticker/GOOGL/range/1/day/2020-06-01/2020-06-17?apiKey=2RsZzwKc4SWPGLSY861uPBABHgbF0kpa")
    data = r.json()
    st.write(data)
if op == "twitter":
    r = requests.get("https://api.polygon.io/v2/aggs/ticker/TW/range/1/day/2020-06-01/2020-06-17?apiKey=2RsZzwKc4SWPGLSY861uPBABHgbF0kpa")
    data = r.json()
    st.write(data)



st.image("https://sp-ao.shortpixel.ai/client/q_glossy,ret_img/https://jingdaily.com/wp-content/uploads/2019/08/shutterstock_1033192045-1240x826.jpg")
