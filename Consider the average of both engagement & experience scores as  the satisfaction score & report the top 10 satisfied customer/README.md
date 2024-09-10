Experience, Engagement, and Satisfaction Score Analysis
This project uses K-Means clustering to compute experience and engagement scores for users based on network performance metrics and derives a satisfaction score. The script identifies the top 10 satisfied customers by sorting them according to their computed satisfaction scores.

Table of Contents
Installation
Dataset
Features
Process Overview
Usage
Results
License
Installation
Ensure that Python and the following libraries are installed:

bash
Copy code
pip install pandas numpy scikit-learn scipy
Dataset
The dataset should be a CSV file that includes network metrics for users such as Avg RTT DL, Avg RTT UL, Avg Bearer TP DL, and others. Modify the file path in the script to point to your dataset:

python
Copy code
file_path = 'D:/10 Acadamy kifiya/Technical Content/data/Week1_challenge_data_source(CSV)'
Features
The script uses the following features for clustering:

Experience Metrics:

Avg RTT DL (ms)
Avg RTT UL (ms)
Avg Bearer TP DL (kbps)
Avg Bearer TP UL (kbps)
TCP DL Retrans. Vol (Bytes)
TCP UL Retrans. Vol (Bytes)
Engagement Metrics: These are assumed to be the same as the experience metrics, but they can be replaced with actual engagement-related metrics if available.

Process Overview
Data Preprocessing:

Missing values in the experience and engagement metrics are replaced with the mean value of each column.
Data is scaled using StandardScaler to improve K-Means clustering performance.
K-Means Clustering:

K-Means clustering is applied separately to experience and engagement metrics with k=3 clusters.
The cluster centroids are computed, and the worst experience and least engaged clusters are identified based on the centroid mean values.
Score Computation:

Experience Score: Calculated as the Euclidean distance from a user’s experience metrics to the centroid of the worst experience cluster.
Engagement Score: Calculated as the Euclidean distance from a user’s engagement metrics to the centroid of the least engaged cluster.
Satisfaction Score:

Calculated as the mean of the engagement and experience scores.
Top 10 Satisfied Customers:

Users are ranked based on their satisfaction scores in ascending order (lower score = higher satisfaction).
The top 10 satisfied customers are displayed and saved to a CSV file.
Usage
Ensure the dataset contains the necessary columns for experience and engagement metrics.
Update the file path in the script to point to your dataset.
Run the script:
bash
Copy code
python customer_satisfaction_analysis.py
The top 10 satisfied customers will be printed in the console, and an optional CSV file with the results will be saved.
Results
The script outputs:

Top 10 Satisfied Customers: Based on the satisfaction score, users are ranked, and the top 10 are identified.
The results are saved to a CSV file at the specified output path:

python
Copy code
output_path = 'D:/10 Acadamy kifiya/Technical Content/data/top_satisfied_customers.csv'
License
This project is open-source and available for modification and use.

