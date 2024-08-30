import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tldextract

# Load the dataset
df = pd.read_csv('raw_analyst_ratings.csv')

# Analyze Publisher Contributions
publisher_counts = df['publisher'].value_counts()

# Plot the top 10 publishers by number of articles
plt.figure(figsize=(12, 6))
publisher_counts.head(10).plot(kind='bar', color='teal')
plt.title('Top 10 Publishers by Number of Articles')
plt.xlabel('Publisher')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Identify unique domains if email addresses are used as publisher names
# Extract the domain from email addresses or URLs
def extract_domain(publisher_name):
    if '@' in publisher_name:  # If it's an email address
        return publisher_name.split('@')[1]
    else:  # If it's a URL or other string, extract the domain
        domain_info = tldextract.extract(publisher_name)
        return f"{domain_info.domain}.{domain_info.suffix}"

df['publisher_domain'] = df['publisher'].apply(extract_domain)

# Count the unique domains
domain_counts = df['publisher_domain'].value_counts()

# Plot the top 10 domains
plt.figure(figsize=(12, 6))
domain_counts.head(10).plot(kind='bar', color='coral')
plt.title('Top 10 Domains by Number of Articles')
plt.xlabel('Domain')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Optional: Analyze the type of news by publisher
# Here you might analyze keywords in the headlines for each publisher
# For simplicity, let's just output the top publishers and their article counts
print("Top 10 Publishers by Number of Articles:")
print(publisher_counts.head(10))

print("\nTop 10 Domains by Number of Articles:")
print(domain_counts.head(10))

