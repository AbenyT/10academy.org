import pandas as pd
import nltk
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('raw_analyst_ratings.csv')

# Text Preprocessing
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Perform Sentiment Analysis on headlines
def analyze_sentiment(headline):
    analysis = TextBlob(headline)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Apply sentiment analysis
df['sentiment'] = df['headline'].apply(analyze_sentiment)

# Display sentiment distribution
sentiment_counts = df['sentiment'].value_counts()
print("\nSentiment Distribution:")
print(sentiment_counts)

# Plotting sentiment distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='sentiment', data=df, order=sentiment_counts.index)
plt.title('Sentiment Analysis of Headlines')
plt.xlabel('Sentiment')
plt.ylabel('Number of Headlines')
plt.show()

# Topic Modeling
# Use CountVectorizer to convert headlines into a matrix of token counts
vectorizer = CountVectorizer(stop_words='english')
doc_term_matrix = vectorizer.fit_transform(df['headline'])

# Set up LDA
lda = LDA(n_components=5, random_state=42)
lda.fit(doc_term_matrix)

# Extracting the topics
def display_topics(model, feature_names, no_top_words):
    topics = {}
    for topic_idx, topic in enumerate(model.components_):
        topic_keywords = [feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]
        topics[topic_idx] = topic_keywords
        print(f"Topic {topic_idx + 1}: {', '.join(topic_keywords)}")
    return topics

# Display the topics
no_top_words = 10
feature_names = vectorizer.get_feature_names_out()
topics = display_topics(lda, feature_names, no_top_words)

# Visualization of topics
for topic_idx, topic_keywords in topics.items():
    plt.figure(figsize=(8, 6))
    sns.barplot(x=topic_keywords, y=lda.components_[topic_idx, [vectorizer.vocabulary_[word] for word in topic_keywords]])
    plt.title(f"Top 10 words for Topic {topic_idx + 1}")
    plt.xlabel('Words')
    plt.ylabel('Importance')
    plt.xticks(rotation=45)
    plt.show()

