import pandas as pd
from textblob import TextBlob
import numpy as np
from scipy.stats import pearsonr
import nltk
from nltk.corpus import stopwords
import string

# Ensure nltk resources are downloaded
nltk.download('stopwords')

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
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    df['Return'] = df['Close'].pct_change() * 100  # Calculate daily returns in percentage
    stock_data[stock] = df

# Load and preprocess news data
news_data = pd.read_csv(news_path, parse_dates=['Date'])
news_data['Date'] = pd.to_datetime(news_data['Date']).dt.date

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

news_data['Cleaned_Headline'] = news_data['Headline'].apply(preprocess_text)
news_data['Sentiment_Score'] = news_data['Cleaned_Headline'].apply(analyze_sentiment)

# Align news sentiment scores with stock data dates
aligned_data = {}
for stock, df in stock_data.items():
    merged_df = pd.merge(df, news_data[['Date', 'Sentiment_Score']], on='Date', how='inner')
    aligned_data[stock] = merged_df

# Print and save correlation results
for stock, df in aligned_data.items():
    correlation, _ = pearsonr(df['Sentiment_Score'], df['Return'].dropna())
    print(f"Correlation between news sentiment and {stock} daily returns: {correlation:.2f}")

# Optionally, save aligned data with sentiment scores
for stock, df in aligned_data.items():
    df.to_csv(f"D:\10 Acadamy kifiya\Technical  Content\Data\yfinance_data\{stock}_aligned_sentiment_data.csv", index=False)
