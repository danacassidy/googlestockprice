import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Dana's Stock Price App

Shown are the stock ***closing price*** and volume of Google!

""")

tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for the ticker
tickerDf = tickerData.history(period='1d', start='2010-4-20', end= '2021-4-20')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)