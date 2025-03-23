import ta

def add_rsi(df, window=14):
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

def add_bollinger_bands(df, window=20):
    rolling_mean = df['Close'].rolling(window=window).mean()
    rolling_std = df['Close'].rolling(window=window).std()
    df['Upper Band'] = rolling_mean + (rolling_std * 2)
    df['Lower Band'] = rolling_mean - (rolling_std * 2)
    return df

def add_sma(df, window=20):
    df[f'SMA_{window}'] = df['Close'].rolling(window=window).mean()
    return df

def add_ema(df, span=20):
    df[f'EMA_{span}'] = df['Close'].ewm(span=span, adjust=False).mean()
    return df


