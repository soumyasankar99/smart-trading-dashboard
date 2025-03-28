
# Smart Trading Dashboard

An **interactive trading assistant** built with **Streamlit**, powered by **Backtrader** and **yFinance**, that brings technical analysis and backtesting to your fingertips - no coding required.

---

## 🚀 Project Overview

In today’s market, traders rely on tools like **TradingView**, but few platforms combine **backtesting**, **multi-stock analysis**, and **indicator customization** in one minimalist UI. This project was born out of the idea to bridge that gap - to create a **zero-setup, fully interactive dashboard** where you can:

- 🧠 Explore indicators like RSI, SMA, EMA, Bollinger Bands  
- 🛠️ Backtest common strategies like RSI-based and SMA crossover  
- 📉 Visualize insights for multiple tickers  
- 📦 Download results as CSV  
- 📊 Analyze volume, trends, and crossovers  
- 🚦 Get actionable buy/sell signals  

---

## 💡 Why This Project?

### 🎯 The Idea Behind It

The goal was to build an app that feels like a trader's **daily tool**: input symbols, choose indicators, apply strategies, and assess market behavior. It should be **quick, interactive, and insightful**. This dashboard achieves that using Streamlit’s frontend and Backtrader’s power under the hood.

### 🧱 Why the Code is Structured Like This

- `app.py`: Manages the **user interface**, visual components, form input, and integration.
- `strategies.py`: Encapsulates **modular trading strategies** used by Backtrader.
- `fetch_data.py`: Handles **data fetching and preprocessing**, ensuring clean, validated inputs.
- `indicators.py`: Calculates selected technical indicators dynamically.
- `backtest.py`: Runs Backtrader's simulation based on user-selected strategy and inputs.

This modular breakdown allows us to **easily add more strategies or indicators** in the future without cluttering the main UI logic.

---

## 🔍 Features

![Smart Trading Dashboard - visual selection (3)](https://github.com/user-attachments/assets/7ba5fa92-6642-4da6-9fa8-957e22c9615a)



| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| ✅ Multi-symbol Support        | Analyze multiple stocks at once (`AAPL, MSFT, TSLA`)                        |
| ✅ Strategy Selector           | Choose from strategies like RSI Strategy, SMA Crossover                     |
| ✅ Indicator Multiselect       | RSI, SMA, EMA, Volume, Bollinger Bands                                     |
| ✅ Data Visualization          | Price charts overlaid with selected indicators                             |
| ✅ Backtesting with Backtrader | Simulates trading performance based on strategy logic                      |
| ✅ CSV Export                  | Download historical data for further analysis                               |
| ✅ Volume Toggle               | Add volume to charts with a switch                                         |
| ✅ Log Scale Toggle            | Helpful for long-term chart viewing                                        |

<img width="958" alt="stock" src="https://github.com/user-attachments/assets/759d47bd-88e5-41f9-ac8e-288febd4168d" />


<img width="963" alt="stock-1" src="https://github.com/user-attachments/assets/9dc51cb9-f625-4bee-9145-296f276d1d13" />


---

## 🧪 Current Strategies


### 📉 1. RSI Strategy – Catching Overbought & Oversold Zones
RSI (Relative Strength Index) is a momentum oscillator that measures the speed and change of price movements on a scale from 0 to 100.

Buy Signal: When RSI < 30
This suggests the asset is oversold—meaning selling pressure may be overdone and a price reversal could be near.

Sell Signal: When RSI > 70
This indicates the asset is overbought, and there may be an upcoming pullback or correction.

✅ Why it works: Traders use RSI to identify possible reversal points. When everyone’s selling or buying too aggressively, the market tends to correct itself.

### 📈 2. SMA Crossover Strategy – Spotting Trend Shifts
SMA (Simple Moving Average) smooths out price data over a specific period.

SMA(20) tracks short-term price movements

SMA(50) tracks medium-term trends

Buy Signal: When SMA(20) crosses above SMA(50)
This is a bullish crossover, signaling upward momentum and the potential start of a trend.

Sell Signal: When SMA(20) crosses below SMA(50)
This is a bearish crossover, suggesting a potential downtrend.

✅ Why it works: This strategy is trend-following—it doesn’t try to predict the market but instead confirms trend direction and helps you ride the wave.

> 🧠 *Why only these two?*  
These are two of the **most widely used, easy-to-understand, and effective** retail trading strategies. Their simplicity makes them great for beginners and easy to visualize during backtesting.

---

## 📂 Folder Structure

![Smart Trading Dashboard - visual selection (4)](https://github.com/user-attachments/assets/51b6b75b-c01c-481d-b372-12c12a2e86fc)


```
smart-trading-dashboard/
│
├── app.py                # Main Streamlit App
├── fetch_data.py         # Historical data fetching and validation
├── indicators.py         # Technical indicators (SMA, EMA, RSI, etc.)
├── strategies.py         # Backtrader trading strategies
├── backtest.py           # Run and plot backtesting logic
├── requirements.txt
└── README.md
```
<img width="959" alt="stock-2" src="https://github.com/user-attachments/assets/33026161-44fd-4547-97a5-fac90e5ce7a9" />

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/soumyasankar99/smart-trading-dashboard.git
cd smart-trading-dashboard
```

### 2. Create and Activate a Virtual Environment
🪟 On Windows:

```bash

python -m venv trading_env
trading_env\Scripts\activate
```
🍏 On macOS:

```bash

python3 -m venv trading_env
source trading_env/bin/activate
```

🐧 On Linux:

```bash

python3 -m venv trading_env
source trading_env/bin/activate
```

> ⚠️ If you face any permission denied error on Linux/macOS, try:
chmod +x trading_env/bin/activate and re-run the source command.

### 3. Install Python Dependencies
```bash

pip install -r requirements.txt
```

### 4. Run the Streamlit App
```bash

streamlit run app.py
```
> The app will automatically open in your browser at http://localhost:8501.

---

## ❗ Obstacles Faced & How I Tackled Them

| Challenge                         | Solution                                                                 |
|----------------------------------|--------------------------------------------------------------------------|
| yFinance returns empty data      | Added **error handling** and **date validation** to notify users         |
| Backtrader throws shape errors   | Restructured input `DataFrame` to fit **Backtrader's format** properly   |
| Streamlit UI crashes on strategy | Modularized code and ensured strategies are only run if selected         |
| Performance issues for large data| Optimized plotting with **Matplotlib** and deferred unnecessary logic    |


## 🧗‍♂️ Development Journey: Mistakes, Fixes & Lessons Learned

While building this, I encountered several tricky bugs and conceptual gaps that taught me a lot. Here’s a transparent breakdown — so that if you're following along, you’re better prepared:

#### ❌ Mistake 1: Wrong Date Range Caused No Data
Problem: Users could accidentally pick an end date before the start date, or select future dates, which caused empty dataframes.

Fix:

Added date validation logic

Used clear Streamlit error messages to guide users

#### ❌ Mistake 2: "Data must be 1-dimensional" Error
Problem: Indicator logic (especially EMA/SMA) returned ndarray instead of 1D Series expected by plotting functions.

Fix:

Flattened data using .ravel() or used .squeeze() when applying NumPy methods

Ensured that matplotlib and Streamlit always receive a 1D data input

#### ❌ Mistake 3: “Only length-1 arrays can be converted to Python scalars”
Problem: While using ax.plot_date() or setting cerebro.adddata(), I was passing arrays not indexed properly.

Fix:

Used .iloc to ensure only one row at a time was processed

Adjusted DataFrame formats to match Backtrader expectations (DatetimeIndex with 'Open', 'High', 'Low', 'Close', 'Volume')

#### ❌ Mistake 4: Only One Strategy Showing in UI
Problem: Even though I wrote multiple strategies, only "RSI Strategy" was showing in the dropdown.

Fix:

Strategy list was hardcoded in Streamlit form

Replaced with a dynamic list pulling from strategies.py dictionary

#### ❌ Mistake 5: Backtrader Plot Not Working in Streamlit
Problem: Backtrader uses its own matplotlib canvas — it doesn't render directly in Streamlit.

Fix:

Replaced cerebro.plot() with custom matplotlib plots

Used matplotlib directly inside Streamlit with st.pyplot(fig)

### 🔬 Why These Strategies?
RSI Strategy: One of the most popular momentum indicators; great for oversold/overbought detection

SMA Crossover: Simple but powerful trend strategy; perfect for learning about crossovers

Bollinger Bands, EMA, SMA, Volume: Commonly used indicators with high signal-to-noise ratio

These choices are educational and practical, perfect for both learning and real-world simulation. The codebase is also ready to expand with more advanced strategies like MACD or Ichimoku.

![Smart Trading Dashboard - visual selection (5)](https://github.com/user-attachments/assets/33d2611d-3a3b-4e22-9502-ad4e80b0742c)


---

## 🔭 Future Improvements

- 📈 Add MACD, Ichimoku Cloud, and more indicators  
- 🤖 Integrate ML models for signal predictions  
- 📦 Save backtest results to local storage or database  
- 💬 Add chatbot-style "trading assistant" to guide beginners  
- 📺 Use real-time data from WebSockets or Alpaca API  
- 💹 Add paper trading and broker API integrations.. Just a few as of now.

---

## 🙌 Contribute or Reach Out

Found a bug, have a feature idea, or want to contribute strategies?  
Feel free to fork, raise issues, or drop a DM. Let's build this trading toolkit together!
