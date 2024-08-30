import pandas as pd
import talib as ta
import matplotlib.pyplot as plt
import pynance as pn

# Load the data
df = pd.read_csv('AAPL_historical_data.csv', parse_dates=['Date'], index_col='Date')

# Display the first few rows to understand the structure
print(df.head())

# Ensure the data includes the required columns
assert all(column in df.columns for column in ['Open', 'High', 'Low', 'Close', 'Volume']), "Missing one or more required columns"

# Apply Analysis Indicators with TA-Lib

# Calculate Moving Averages
df['SMA_50'] = ta.SMA(df['Close'], timeperiod=50)
df['SMA_200'] = ta.SMA(df['Close'], timeperiod=200)

# Calculate RSI (Relative Strength Index)
df['RSI'] = ta.RSI(df['Close'], timeperiod=14)

# Calculate MACD (Moving Average Convergence Divergence)
df['MACD'], df['MACD_Signal'], df['MACD_Hist'] = ta.MACD(df['Close'], 
                                                          fastperiod=12, 
                                                          slowperiod=26, 
                                                          signalperiod=9)

# Display the DataFrame with new columns
print(df[['Close', 'SMA_50', 'SMA_200', 'RSI', 'MACD', 'MACD_Signal']].tail())

# Use PyNance for Financial Metrics (Example Placeholder)

# Fetch additional data with PyNance (example, adjust as needed)
# pn.ta.get('AAPL')  # Fetch AAPL data from a finance API

# Visualize the Data

# Plotting the stock price with moving averages
plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['SMA_50'], label='50-Day SMA', color='red')
plt.plot(df['SMA_200'], label='200-Day SMA', color='green')
plt.title('AAPL Close Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Plotting RSI
plt.figure(figsize=(14, 7))
plt.plot(df['RSI'], label='RSI', color='purple')
plt.title('AAPL RSI')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.axhline(70, linestyle='--', color='red', label='Overbought (70)')
plt.axhline(30, linestyle='--', color='green', label='Oversold (30)')
plt.legend()
plt.show()

# Plotting MACD
plt.figure(figsize=(14, 7))
plt.plot(df['MACD'], label='MACD', color='blue')
plt.plot(df['MACD_Signal'], label='Signal Line', color='red')
plt.bar(df.index, df['MACD_Hist'], label='MACD Histogram', color='gray')
plt.title('AAPL MACD')
plt.xlabel('Date')
plt.ylabel('MACD')
plt.legend()
plt.show()

