import pandas as pd

# Define paths
stock_files = {
    "AAPL": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\AAPL_historical_data.csv",
    "AMZN": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\AMZN_historical_data.csv",
    "GOOG": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\GOOG_historical_data.csv",
    "META": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\META_historical_data.csv",
    "MSFT": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\MSFT_historical_data.csv",
    "NVDA": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\NVDA_historical_data.csv"
}

news_path = r"D:\10 Acadamy kifiya\Technical  Content\Data\raw_analyst_ratings.csv"

# Load stock data
stock_data = {}
for stock, path in stock_files.items():
    df = pd.read_csv(path, parse_dates=['Date'])
    df['Date'] = pd.to_datetime(df['Date']).dt.date  # Normalize dates to just the date part
    stock_data[stock] = df

# Load and preprocess news data
news_data = pd.read_csv(news_path, parse_dates=['Date'])
news_data['Date'] = pd.to_datetime(news_data['Date']).dt.date  # Normalize dates to just the date part

# Align dates
aligned_data = {}
for stock, df in stock_data.items():
    # Merge stock data with news data on Date
    merged_df = pd.merge(df, news_data[['Date', 'Sentiment_Score']], on='Date', how='left')
    
    # Handle missing sentiment scores for stock trading days without news
    merged_df['Sentiment_Score'].fillna(method='ffill', inplace=True)  # Forward fill missing sentiment scores
    
    aligned_data[stock] = merged_df

# Print sample data to verify alignment
for stock, df in aligned_data.items():
    print(f"\nSample of aligned data for {stock}:")
    print(df[['Date', 'Close', 'Return', 'Sentiment_Score']].head())

# Optionally, save the aligned data to new CSV files
for stock, df in aligned_data.items():
    df.to_csv(f"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\{stock}_aligned_data.csv", index=False)

