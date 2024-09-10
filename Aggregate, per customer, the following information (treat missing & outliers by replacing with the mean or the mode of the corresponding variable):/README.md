Overview
This script is designed to load, preprocess, and aggregate customer network experience data from a CSV file. The script cleans the data by handling missing values and outliers, then aggregates the data per customer. The aggregated data is then saved to a new CSV file for further analysis.

Features:
Handles missing values for numerical and categorical data.
Removes outliers by replacing them with the mean value.
Aggregates network experience metrics for each customer.
Saves the processed data to a new CSV file.
Libraries Used:
pandas: For data manipulation and aggregation.
numpy: For numerical operations and handling outliers.
Input Data:
The CSV file should contain the following columns (or similar):

customer_id: Unique identifier for each customer.
tcp_retransmission: TCP retransmission data (numerical).
rtt: Round-trip time data (numerical).
throughput: Throughput data (numerical).
handset_type: Type of handset used by the customer (categorical).
Preprocessing Steps:
Missing Values Handling:

Missing values in numerical columns (tcp_retransmission, rtt, throughput) are replaced with the mean of the respective columns.
Missing values in the categorical column (handset_type) are replaced with the mode (most frequent value).
Outlier Handling:

For numerical columns, any value beyond the 99th percentile is considered an outlier and replaced with the column mean.
Data Aggregation:

Data is grouped by customer_id, and the mean of tcp_retransmission, rtt, and throughput is calculated.
For the handset_type column, the mode (most common handset) is selected for each customer.
Instructions to Run:
Install the necessary libraries if they are not installed:
Copy code
pip install pandas numpy
Modify the file_path variable to point to your input CSV file.
Run the script in your Python environment.
The script will:
Load the CSV file and display the first few rows.
Replace missing values and handle outliers.
Aggregate the data by customer.
Display the first few rows of the aggregated data.
Save the aggregated data to a new CSV file (aggregated_customer_data.csv).
File Paths:
Input CSV File: The script reads data from a file specified by the file_path variable. Update the path to the location of your input file.
Output CSV File: Aggregated data is saved to aggregated_customer_data.csv. You can change the output_file_path variable to specify a different location or filename.
Example Usage:
Modify the file_path and output_file_path in the script to match your file locations.
Run the script, and the aggregated data will be saved to a new CSV file.
Notes:
Adjust the column names in the code based on the actual columns in your dataset.
The outlier handling threshold (99th percentile) can be modified based on the data distribution.
