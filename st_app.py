import streamlit as st
import yfinance as yf
import pandas

st.write(""" 
# simple Stock Price App

Apple Closing Stock Price and Volumes
""")

tickerSymbol ="AAPL"
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start = '2023-5-31', end='2024-1-20')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
