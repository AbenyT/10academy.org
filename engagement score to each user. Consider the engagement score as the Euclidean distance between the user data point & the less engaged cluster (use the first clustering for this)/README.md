Overview
This project applies K-Means Clustering on network metrics such as TCP Retransmission, RTT, and Throughput to group users into clusters. Additionally, it calculates an engagement score for each user based on their distance from the least engaged cluster.

The project uses Scikit-learn for clustering and data normalization, SciPy for distance calculations, and Pandas for data handling.

Requirements
Python 3.x
Pip package manager
Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
cd <repository_folder>
Install the required packages using pip:

bash
Copy code
pip install -r requirements.txt
If you don't have a requirements.txt file, manually install the required packages:

bash
Copy code
pip install pandas numpy scikit-learn scipy
Dataset
This project uses a CSV dataset with the following columns:

tcp_retransmission: TCP retransmission count (a higher number indicates more network issues)
rtt: Round-trip time of network packets (higher values imply delays)
throughput: Data throughput (lower values can indicate poor performance)
The dataset should be in the file path specified in the script. You can replace the file_path variable with the actual path to your dataset.

How to Run the Code
Prepare your dataset: Ensure your dataset is available and formatted correctly. Update the file_path variable in the script with the correct path to your dataset.

Run the script:

Execute the Python script using the following command:

bash
Copy code
python <script_name>.py
The script will:

Load and preprocess the data by handling missing values (replacing them with the column mean).
Normalize the data to prepare it for K-Means clustering.
Apply K-Means Clustering with k=3 clusters.
Identify the centroids of each cluster and convert them back to the original scale for interpretation.
Calculate the Engagement Score for each user based on their Euclidean distance from the least engaged cluster.
Save the results (including cluster assignments and engagement scores) to a CSV file.
Output:

The script will print the cluster centroids in the original data scale.
It will also display the first few rows of the dataset with the cluster assignments and engagement scores.
Save Results: The final dataset, including the cluster assignments and engagement scores, will be saved as a CSV file named user_engagement_scores.csv in the working directory.

Key Components
Data Preprocessing:

Missing values in tcp_retransmission, rtt, and throughput columns are handled by replacing them with the mean of the respective columns.
Data Normalization:

The feature columns are scaled using StandardScaler from Scikit-learn to ensure that K-Means clustering works effectively, as it is a distance-based algorithm.
K-Means Clustering:

The dataset is clustered into 3 groups using the K-Means algorithm. Cluster centers (centroids) are identified and converted back to the original scale for easier interpretation.
Engagement Score Calculation:

The Euclidean distance between each user's experience metrics and the least engaged cluster's centroid is calculated to assign an engagement score. A lower score indicates better engagement.
Customization
Number of Clusters: You can change the number of clusters by modifying the n_clusters parameter:

python
Copy code
kmeans = KMeans(n_clusters=4, random_state=42)
File Paths: Update the file_path and the output path for saving the final CSV:

python
Copy code
file_path = 'your_file_path.csv'
output_path = 'your_output_path.csv'
Features: If you have more or different features, adjust the features variable to include those columns:

python
Copy code
features = df[['your_column_1', 'your_column_2', ...]]
Files
script_name.py: The main Python script that handles data preprocessing, clustering, engagement score calculation, and saving results.
user_engagement_scores.csv: The output CSV file that includes the original data, cluster assignments, and calculated engagement scores.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
