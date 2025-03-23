import backtrader as bt

class RSI_Strategy(bt.Strategy):
    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close)
    def next(self):
        if not self.position and self.rsi < 30:
            self.buy()
        elif self.position and self.rsi > 70:
            self.sell()

class SMA_CrossStrategy(bt.Strategy):
    def __init__(self):
        self.sma1 = bt.indicators.SMA(self.data.close, period=20)
        self.sma2 = bt.indicators.SMA(self.data.close, period=50)
    def next(self):
        if self.sma1[0] > self.sma2[0] and self.sma1[-1] < self.sma2[-1]:
            self.buy()
        elif self.sma1[0] < self.sma2[0] and self.sma1[-1] > self.sma2[-1]:
            self.sell()

def run_backtest(df, strategy_name):
    data = bt.feeds.PandasData(dataname=df.set_index("Date"))
    cerebro = bt.Cerebro()
    if strategy_name == "RSI Strategy":
        cerebro.addstrategy(RSI_Strategy)
    elif strategy_name == "SMA Crossover":
        cerebro.addstrategy(SMA_CrossStrategy)
    cerebro.adddata(data)
    cerebro.run()
    cerebro.plot()
