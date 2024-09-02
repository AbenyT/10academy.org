import pandas as pd
from textblob import TextBlob
import string
import nltk
from nltk.corpus import stopwords

# Ensure nltk resources are downloaded
nltk.download('stopwords')

# Define path for the news data
news_path = r"D:\10 Acadamy kifiya\Technical  Content\Data\raw_analyst_ratings.csv"

# Load and preprocess news data
news_data = pd.read_csv(news_path, parse_dates=['Date'])
news_data['Date'] = pd.to_datetime(news_data['Date']).dt.date  # Normalize dates to just the date part

# Function to preprocess text
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

# Apply preprocessing to the headlines
news_data['Cleaned_Headline'] = news_data['Headline'].apply(preprocess_text)

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Polarity score between -1 and 1

# Apply sentiment analysis to the cleaned headlines
news_data['Sentiment_Score'] = news_data['Cleaned_Headline'].apply(analyze_sentiment)

# Display the first few rows of the dataframe to verify sentiment scores
print(news_data[['Date', 'Headline', 'Sentiment_Score']].head())

# Optionally, save the sentiment scores to a new CSV file
news_data.to_csv(r"D:\10 Acadamy kifiya\Technical  Content\Data\news_sentiment_scores.csv", index=False)
