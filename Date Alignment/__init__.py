import pandas as pd

# Define the paths to the stock prices data
stock_files = {
    "AAPL": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\AAPL_historical_data.csv",
    "AMZN": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\AMZN_historical_data.csv",
    "GOOG": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\GOOG_historical_data.csv",
    "META": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\META_historical_data.csv",
    "MSFT": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\MSFT_historical_data.csv",
    "NVDA": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\NVDA_historical_data.csv"
}

# Load the stock prices data
stock_data = {}
for stock, path in stock_files.items():
    df = pd.read_csv(path, parse_dates=['Date'])
    stock_data[stock] = df

# Define the path to the news data
news_path = r"D:\10 Acadamy kifiya\Technical  Content\Data\raw_analyst_ratings.csv"

# Load the news data
news_data = pd.read_csv(news_path, parse_dates=['Date'])

# Normalize timestamps in the news data
news_data['Date'] = pd.to_datetime(news_data['Date']).dt.date

# Normalize timestamps in stock prices data
for stock, df in stock_data.items():
    df['Date'] = pd.to_datetime(df['Date']).dt.date

# Align dates
aligned_data = {}
for stock, df in stock_data.items():
    aligned_data[stock] = df[df['Date'].isin(news_data['Date'])]
    print(f"\nAligned data for {stock}:")
    print(aligned_data[stock].head())

# Optionally, reindex news data to only include dates that match the stock prices
news_data_aligned = news_data[news_data['Date'].isin(stock_data['AAPL']['Date'])]  # Using AAPL's dates for alignment
print("\nAligned news data:")
print(news_data_aligned.head())

# Save the aligned data if necessary
for stock, df in aligned_data.items():
    df.to_csv(f"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\{stock}_aligned_data.csv", index=False)

news_data_aligned.to_csv(r"D:\10 Acadamy kifiya\Technical  Content\Data\news_aligned_data.csv", index=False)
