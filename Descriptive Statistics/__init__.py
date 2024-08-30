import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('raw_analyst_ratings.csv')

# Display the first few rows of the dataset
print(df.head())

# Descriptive Statistics

# 1. Obtain basic statistics for textual lengths (like headline length)
df['headline_length'] = df['headline'].apply(len)
headline_stats = df['headline_length'].describe()
print("\nHeadline Length Statistics:")
print(headline_stats)

# Plotting the distribution of headline lengths
plt.figure(figsize=(10, 6))
sns.histplot(df['headline_length'], kde=True, bins=30)
plt.title('Distribution of Headline Lengths')
plt.xlabel('Headline Length')
plt.ylabel('Frequency')
plt.show()

# 2. Count the number of articles per publisher
publisher_counts = df['publisher'].value_counts()
print("\nNumber of Articles per Publisher:")
print(publisher_counts)

# Plotting the number of articles per publisher
plt.figure(figsize=(12, 8))
publisher_counts.plot(kind='bar')
plt.title('Number of Articles per Publisher')
plt.xlabel('Publisher')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.show()

# 3. Analyze the publication dates to see trends over time

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Extracting day of the week, month, and hour for further analysis
df['day_of_week'] = df['date'].dt.day_name()
df['month'] = df['date'].dt.month_name()
df['hour'] = df['date'].dt.hour

# Number of articles per day of the week
day_of_week_counts = df['day_of_week'].value_counts()
print("\nNumber of Articles per Day of the Week:")
print(day_of_week_counts)

# Plotting the number of articles per day of the week
plt.figure(figsize=(10, 6))
sns.countplot(x='day_of_week', data=df, order=day_of_week_counts.index)
plt.title('Number of Articles per Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.show()

# Number of articles per month
month_counts = df['month'].value_counts()
print("\nNumber of Articles per Month:")
print(month_counts)

# Plotting the number of articles per month
plt.figure(figsize=(10, 6))
sns.countplot(x='month', data=df, order=month_counts.index)
plt.title('Number of Articles per Month')
plt.xlabel('Month')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.show()

# Number of articles per hour
hour_counts = df['hour'].value_counts().sort_index()
print("\nNumber of Articles per Hour:")
print(hour_counts)

# Plotting the number of articles per hour
plt.figure(figsize=(10, 6))
sns.lineplot(x=hour_counts.index, y=hour_counts.values)
plt.title('Number of Articles per Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Articles')
plt.show()

# Trend Analysis Over Time

# Resampling to see the number of articles per day, week, and month
daily_counts = df.resample('D', on='date').size()
weekly_counts = df.resample('W', on='date').size()
monthly_counts = df.resample('M', on='date').size()

# Plotting trends over time
plt.figure(figsize=(14, 8))
plt.plot(daily_counts, label='Daily')
plt.plot(weekly_counts, label='Weekly')
plt.plot(monthly_counts, label='Monthly')
plt.title('Number of Articles Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.legend()
plt.show()

