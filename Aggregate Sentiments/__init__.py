import pandas as pd

# Load the news data with sentiment scores
news_path = r"D:\10 Acadamy kifiya\Technical  Content\Data\raw_analyst_ratings.csv"
news_data = pd.read_csv(news_path, parse_dates=['Date'])

# Assume sentiment scores were already calculated in a previous step
# If not, include the sentiment analysis step here
news_data['Date'] = pd.to_datetime(news_data['Date']).dt.date  # Normalize dates to just the date part

# Aggregate sentiment scores by date
average_daily_sentiment = news_data.groupby('Date')['Sentiment_Score'].mean().reset_index()

# Print the first few rows of the aggregated sentiment scores
print("Average Daily Sentiment Scores:")
print(average_daily_sentiment.head())

# Optionally, save the average daily sentiment scores to a new CSV file
output_path = r"D:\10 Acadamy kifiya\Technical  Content\Data\average_daily_sentiment.csv"
average_daily_sentiment.to_csv(output_path, index=False)

# Print confirmation of saved file
print(f"\nAverage daily sentiment scores saved to: {output_path}")
