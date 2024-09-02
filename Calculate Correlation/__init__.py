import pandas as pd

# Load the average daily sentiment data
sentiment_path = r"D:\10 Acadamy kifiya\Technical  Content\Data\average_daily_sentiment.csv"
average_daily_sentiment = pd.read_csv(sentiment_path, parse_dates=['Date'])

# Load the stock daily returns data
stock_paths = {
    "AAPL": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\AAPL_daily_returns.csv",
    "AMZN": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\AMZN_daily_returns.csv",
    "GOOG": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\GOOG_daily_returns.csv",
    "META": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\META_daily_returns.csv",
    "MSFT": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\MSFT_daily_returns.csv",
    "NVDA": r"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\NVDA_daily_returns.csv"
}

# Initialize a dictionary to store correlation results
correlations = {}

# Merge sentiment data with stock returns data and calculate correlation for each stock
for stock, path in stock_paths.items():
    stock_data = pd.read_csv(path, parse_dates=['Date'])
    merged_data = pd.merge(average_daily_sentiment, stock_data[['Date', 'Daily_Return']], on='Date')
    
    # Calculate Pearson correlation coefficient
    correlation = merged_data['Sentiment_Score'].corr(merged_data['Daily_Return'])
    correlations[stock] = correlation
    
    # Print the correlation for the current stock
    print(f"Pearson correlation between average daily sentiment and {stock} daily returns: {correlation:.4f}")

# Optionally, save the correlation results to a new CSV file
correlation_df = pd.DataFrame(list(correlations.items()), columns=['Stock', 'Correlation'])
output_path = r"D:\10 Acadamy kifiya\Technical  Content\Data\sentiment_stock_correlation.csv"
correlation_df.to_csv(output_path, index=False)

# Print confirmation of saved file
print(f"\nCorrelation results saved to: {output_path}")
