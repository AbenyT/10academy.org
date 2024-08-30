# Financial News Publisher Analysis

This repository contains a Python script for performing publisher analysis on a dataset of financial news headlines. The analysis focuses on identifying the most active publishers, understanding the types of news they report, and analyzing the domains associated with publisher email addresses or URLs.

## Dataset

The dataset used for this analysis is `raw_analyst_ratings.csv`, which contains the following columns:

- `headline`: The title of the news article, often including key financial actions like stocks hitting highs, price target changes, or company earnings.
- `url`: The direct link to the full news article.
- `publisher`: The author or creator of the article.
- `date`: The publication date and time, including timezone information (UTC-4 timezone).
- `stock`: The stock ticker symbol (a unique series of letters assigned to a publicly traded company). For example, `AAPL` for Apple.

## Requirements

To run the analysis, you will need the following Python libraries:

- pandas
- matplotlib
- seaborn
- tldextract

You can install the required libraries using the following command:

```bash
pip install pandas matplotlib seaborn tldextract

