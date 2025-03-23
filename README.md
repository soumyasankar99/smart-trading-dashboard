
# Smart Trading Dashboard

An **interactive trading assistant** built with **Streamlit**, powered by **Backtrader** and **yFinance**, that brings technical analysis and backtesting to your fingertips — no coding required.

---

## 🚀 Project Overview

In today’s market, traders rely on tools like **TradingView**, but few platforms combine **backtesting**, **multi-stock analysis**, and **indicator customization** in one minimalist UI. This project was born out of the idea to bridge that gap — to create a **zero-setup, fully interactive dashboard** where you can:

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

---

## 🧪 Current Strategies

### 1. **RSI Strategy**
- **Buy** when RSI < 30  
- **Sell** when RSI > 70  
Ideal for detecting oversold/overbought conditions.

### 2. **SMA Crossover Strategy**
- **Buy** when SMA(20) crosses above SMA(50)  
- **Sell** when SMA(20) crosses below SMA(50)  
Captures **trend reversals** and momentum signals.

> 🧠 *Why only these two?*  
These are two of the **most widely used, easy-to-understand, and effective** retail trading strategies. Their simplicity makes them great for beginners and easy to visualize during backtesting.

---

## 📂 Folder Structure

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

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/smart-trading-dashboard.git
cd smart-trading-dashboard
```

### 2. Create and activate a virtual environment

```bash
python -m venv trading_env
source trading_env/bin/activate  # On Windows: trading_env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

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
