import streamlit as st
from api_key import api_key
from coinpaprika import client as cp
import pandas as pd

client = cp.Client(api_key=api_key)

st.header("Crypto Dashboard")