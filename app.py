import streamlit as st
import matplotlib.pyplot as plt
from fetch_data import fetch_data
from indicators import add_rsi, add_bollinger_bands, add_sma, add_ema

st.set_page_config(layout="wide")
st.title("\U0001F4C8 Smart Trading Dashboard")

# Inputs
symbols_input = st.text_input("Enter stock symbols (comma separated):", "AAPL, MSFT")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

indicators = st.multiselect(
    "Select indicators:",
    ['SMA', 'EMA', 'RSI', 'Bollinger Bands', 'Volume']
)

strategy = st.selectbox("Select strategy:", ["RSI Strategy", "SMA Crossover"])



log_scale = st.toggle("Use log scale")

if st.button("Analyze"):
    symbols = [s.strip().upper() for s in symbols_input.split(',')]

    for symbol in symbols:
        try:
            df = fetch_data(symbol, start_date, end_date)

            # Apply indicators
            if 'RSI' in indicators:
                df = add_rsi(df)
            if 'Bollinger Bands' in indicators:
                df = add_bollinger_bands(df)
            if 'SMA' in indicators:
                df = add_sma(df, window=20)
            if 'EMA' in indicators:
                df = add_ema(df, span=20)

            st.subheader(f"{symbol} Price & Indicators")
            fig, ax = plt.subplots(figsize=(14, 6))
            ax.plot(df.index, df['Close'], label='Close', color='black')

            if 'SMA' in indicators:
                ax.plot(df.index, df['SMA_20'], label='SMA 20', linestyle='--')
            if 'EMA' in indicators:
                ax.plot(df.index, df['EMA_20'], label='EMA 20', linestyle='--')
            if 'Bollinger Bands' in indicators:
                ax.plot(df.index, df['Upper Band'], label='Upper Band', linestyle='--')
                ax.plot(df.index, df['Lower Band'], label='Lower Band', linestyle='--')

            ax.set_title(f"{symbol} Stock Price")
            ax.set_ylabel("Price")
            ax.legend()
            if log_scale:
                ax.set_yscale("log")
            st.pyplot(fig)

            # Volume
            if 'Volume' in indicators:
                fig2, ax2 = plt.subplots(figsize=(14, 2))
                ax2.bar(df.index, df['Volume'], label='Volume', color='skyblue')
                ax2.set_title("Volume")
                st.pyplot(fig2)

            # RSI
            if 'RSI' in indicators:
                fig3, ax3 = plt.subplots(figsize=(14, 2))
                ax3.plot(df.index, df['RSI'], label='RSI', color='purple')
                ax3.axhline(70, linestyle='--', color='red')
                ax3.axhline(30, linestyle='--', color='green')
                ax3.set_title("RSI")
                st.pyplot(fig3)

            # Download CSV
            st.download_button(
                label=f"Download {symbol} data as CSV",
                data=df.to_csv().encode('utf-8'),
                file_name=f"{symbol}_data.csv",
                mime='text/csv'
            )

        except Exception as e:
            st.error(f"{symbol}: {str(e)}")
