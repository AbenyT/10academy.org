import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('raw_analyst_ratings.csv')

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], utc=True)

# Extract date and time components
df['date_only'] = df['date'].dt.date
df['time_only'] = df['date'].dt.time
df['hour'] = df['date'].dt.hour
df['day_of_week'] = df['date'].dt.day_name()

# Publication Frequency Over Time
# Group by date and count the number of articles published each day
daily_publication_counts = df.groupby('date_only').size()

# Plot the publication frequency over time
plt.figure(figsize=(12, 6))
daily_publication_counts.plot(title='Daily Publication Frequency Over Time', color='blue')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.grid(True)
plt.show()

# Analyzing Spikes in Publication Frequency
# Identify days with unusually high publication frequency
mean_publications = daily_publication_counts.mean()
std_publications = daily_publication_counts.std()
spike_threshold = mean_publications + 2 * std_publications
spike_days = daily_publication_counts[daily_publication_counts > spike_threshold]

print(f"Spike Days (Articles > {spike_threshold:.2f}):")
print(spike_days)

# Analysis of Publishing Times
# Group by hour and count the number of articles published in each hour
hourly_publication_counts = df.groupby('hour').size()

# Plot the distribution of publishing times
plt.figure(figsize=(12, 6))
sns.barplot(x=hourly_publication_counts.index, y=hourly_publication_counts.values, palette='viridis')
plt.title('Publication Frequency by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Articles')
plt.grid(True)
plt.show()

# Analyze publication frequency by day of the week
weekday_publication_counts = df.groupby('day_of_week').size()
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

plt.figure(figsize=(12, 6))
sns.barplot(x=weekday_order, y=weekday_publication_counts.reindex(weekday_order), palette='coolwarm')
plt.title('Publication Frequency by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Articles')
plt.grid(True)
plt.show()

