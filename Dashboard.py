import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen

st.title("Cryptocurrency Financial Dashboard")
st.header("Main Dashboard")
# st.subheader("keep track of most important currencies")

Bitcoin = "BTC-USD"
Ethereum = "ETH-USD"
Ripple = "XRP-USD"

BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)

BTC_His = BTC_Data.history(period="max")
ETH_His = ETH_Data.history(period="max")
XRP_His = XRP_Data.history(period="max")

BTC = yf.download(Bitcoin, start="2021-11-18", end="2021-11-19")
ETH = yf.download(Ethereum, start="2021-11-18", end="2021-11-19")
XRP = yf.download(Ripple, start="2021-11-18", end="2021-11-19")

st.write("Bitcoin ($)")
imageBTC = Image.open(
    urlopen(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Bitcoin_logo.svg/2560px-Bitcoin_logo.svg.png"
    )
)
st.image(imageBTC)

st.table(BTC)

st.bar_chart(BTC_His.Close)


st.write("Ethereum ($)")
imageETH = Image.open(
    urlopen(
        "https://ethereum.org/static/c3bcc8c47890ffd2a2c329972c73d0fd/e018d/ethereum-logo-portrait-black-gray.png"
    )
)
st.image(imageETH)

st.table(ETH)

st.bar_chart(ETH_His.Close)


st.write("Ripple ($)")
imageXRP = Image.open(
    urlopen("https://www.vectorlogo.zone/logos/ripple/ripple-ar21.png")
)
st.image(imageXRP)

st.table(XRP)

st.bar_chart(XRP_His.Close)
