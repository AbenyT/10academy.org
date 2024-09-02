import pandas as pd
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
import string

# Ensure that nltk resources are downloaded
nltk.download('stopwords')

# Define the path to the news data
news_path = r"D:\10 Acadamy kifiya\Technical  Content\Data\raw_analyst_ratings.csv"

# Load the news data
news_data = pd.read_csv(news_path, parse_dates=['Date'])

# Define a function for text preprocessing
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]  # Remove stopwords
    return ' '.join(words)

# Apply preprocessing to the 'Headline' column
news_data['Cleaned_Headline'] = news_data['Headline'].apply(preprocess_text)

# Define a function for sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis
news_data['Sentiment'] = news_data['Cleaned_Headline'].apply(analyze_sentiment)

# Save the results to a new CSV file
sentiment_path = r"D:\10 Acadamy kifiya\Technical  Content\Data\news_sentiment_analysis.csv"
news_data.to_csv(sentiment_path, index=False)

# Print some results
print("Sample Sentiment Analysis Results:")
print(news_data[['Date', 'Headline', 'Sentiment']].head())
