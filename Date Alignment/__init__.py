import pandas as pd

# Load the stock prices data
stock_files = [
    "AAPL_historical_data.csv",
    "AMZN_historical_data.csv",
    "GOOG_historical_data.csv",
    "META_historical_data.csv",
    "MSFT_historical_data.csv",
    "NVDA_historical_data.csv"
]

stock_data = {}
for file in stock_files:
    df = pd.read_csv(file, parse_dates=['Date'])
    stock_data[file.split('_')[0]] = df

# Load the news data
news_data = pd.read_csv("raw_analyst_ratings.csv", parse_dates=['Date'])

# Normalize timestamps in the news data
news_data['Date'] = pd.to_datetime(news_data['Date']).dt.date

# Normalize timestamps in stock prices data
for stock, df in stock_data.items():
    df['Date'] = pd.to_datetime(df['Date']).dt.date

# Align dates
aligned_data = {}
for stock, df in stock_data.items():
    aligned_data[stock] = df[df['Date'].isin(news_data['Date'])]

# Optionally, reindex news data to only include dates that match the stock prices
news_data_aligned = news_data[news_data['Date'].isin(df['Date'])]

# Save the aligned data if necessary
for stock, df in aligned_data.items():
    df.to_csv(f"{stock}_aligned_data.csv", index=False)

news_data_aligned.to_csv("news_aligned_data.csv", index=False)
