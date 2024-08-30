# Financial News Dataset Analysis

This repository contains a Python script for analyzing a dataset of financial news headlines. The analysis focuses on various descriptive statistics, publisher contributions, and trends over time.

## Dataset

The dataset used for this analysis is `raw_analyst_ratings.csv`, which contains the following columns:

- `headline`: The title of the news article, often including key financial actions like stocks hitting highs, price target changes, or company earnings.
- `url`: The direct link to the full news article.
- `publisher`: The author or creator of the article.
- `date`: The publication date and time, including timezone information.
- `stock`: The stock ticker symbol (a unique series of letters assigned to a publicly traded company).

## Analysis Overview

The analysis is divided into several key sections:

### 1. Descriptive Statistics

- **Headline Length Analysis**: The script calculates the length of each headline and provides basic statistics (mean, median, etc.) on these lengths. A histogram is plotted to visualize the distribution of headline lengths.

### 2. Publisher Analysis

- **Articles per Publisher**: The script counts the number of articles contributed by each publisher and visualizes the top publishers using a bar chart.

### 3. Time Series Analysis

- **Publication Trends**: The script analyzes the publication dates and times to identify trends. This includes:
  - The number of articles published per day of the week.
  - The number of articles published per month.
  - The number of articles published at different hours of the day.

- **Trend Analysis Over Time**: The script resamples the data to observe the number of articles published on a daily, weekly, and monthly basis, and visualizes these trends over time.

## Requirements

To run the analysis, you will need the following Python libraries:

- pandas
- numpy
- matplotlib
- seaborn

You can install the required libraries using the following command:

```bash
pip install pandas numpy matplotlib seaborn

