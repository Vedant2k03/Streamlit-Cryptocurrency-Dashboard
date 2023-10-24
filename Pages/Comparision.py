import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Cryptocurrencies vs Stocks")

tickers = ("TSLA", "AAPL", "MSFT", "BTC-USD", "ETH-USD", "XRP-USD")

dropdown = st.multiselect("Pick your assets", tickers)

start = st.date_input("Start", value=pd.to_datetime("2023-01-01"))
end = st.date_input("End", value=pd.to_datetime("today"))


def relativeReturn(df):
    rel = df.pct_change()
    cumReturn = (1 + rel).cumprod() - 1
    cumReturn = cumReturn.fillna(0)
    return cumReturn


if len(dropdown) > 0:
    # df = yf.download(dropdown, start, end)['Adj Close']
    df = relativeReturn(yf.download(dropdown, start, end)["Adj Close"])
    st.header("Returns of {}".format(dropdown))
    st.line_chart(df)
