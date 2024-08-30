AAPL Stock Analysis with Python
This repository contains Python code for performing quantitative analysis on Apple Inc. (AAPL) stock data. The analysis includes the application of various technical indicators using TA-Lib and financial metrics using PyNance. Additionally, it provides visualizations to help understand the stock's performance over time.

Features
Data Loading and Preparation:

Load historical stock price data.
Ensure data includes essential columns such as Open, High, Low, Close, and Volume.
Technical Indicators with TA-Lib:

Simple Moving Averages (SMA): 50-day and 200-day SMAs to track the trend.
Relative Strength Index (RSI): A momentum oscillator to measure price movement speed and changes.
Moving Average Convergence Divergence (MACD): A trend-following momentum indicator that reveals changes in the strength, direction, momentum, and duration of a trend.
Financial Metrics with PyNance:

Placeholder for extending the analysis with additional financial data and metrics using the PyNance library.
Visualization:

Plots for the stock price with moving averages.
RSI plots with overbought and oversold levels.
MACD plots including the MACD line, Signal line, and Histogram.
Prerequisites
Ensure you have the following Python libraries installed:

bash
Copy code
pip install pandas matplotlib ta-lib pynance
Data
AAPL_historical_data.csv: The historical stock price data for Apple Inc. (AAPL). Ensure this file is placed in the root directory of the project.
Usage
Clone the repository:


Ensure the AAPL_historical_data.csv file is in the root directory of the project.
Run the Script:

Execute the Python script to perform the analysis:
bash
Copy code
python stock_analysis.py
The script will load the data, apply technical indicators, and generate visualizations.
Visualizations
The script generates the following visualizations:

AAPL Close Price with Moving Averages: Displays the stock's closing price along with the 50-day and 200-day SMAs.
AAPL RSI: Plots the RSI with overbought (70) and oversold (30) thresholds.
AAPL MACD: Shows the MACD line, Signal line, and Histogram.
Extending the Analysis
PyNance: Use PyNance to fetch and analyze additional financial metrics.
Additional Indicators: Explore more indicators from TA-Lib to enrich your analysis.
Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
