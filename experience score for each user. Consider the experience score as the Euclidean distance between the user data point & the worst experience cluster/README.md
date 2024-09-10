Overview
This project uses K-Means Clustering to analyze network performance metrics such as RTT (Round Trip Time), throughput, and TCP retransmission volumes. It calculates an experience score for each user by measuring their distance from the worst-performing cluster, based on certain network performance characteristics.

The project uses Scikit-learn for clustering and data scaling, SciPy for distance calculations, and Pandas for data manipulation.

Requirements
Python 3.x
Pip package manager
Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
cd <repository_folder>
Install the required libraries using pip:

bash
Copy code
pip install -r requirements.txt
Alternatively, if you don't have a requirements.txt file, install the necessary packages manually:

bash
Copy code
pip install pandas numpy scikit-learn scipy
Dataset
The dataset should include the following columns:

Avg RTT DL (ms) (Average Round Trip Time Download in milliseconds)
Avg RTT UL (ms) (Average Round Trip Time Upload in milliseconds)
Avg Bearer TP DL (kbps) (Average Bearer Throughput Download in kbps)
Avg Bearer TP UL (kbps) (Average Bearer Throughput Upload in kbps)
TCP DL Retrans. Vol (Bytes) (TCP Download Retransmission Volume in Bytes)
TCP UL Retrans. Vol (Bytes) (TCP Upload Retransmission Volume in Bytes)
MSISDN/Number (Unique identifier for each user)
The dataset path should be correctly defined in the script by updating the file_path variable.

How to Run the Code
Prepare your dataset: Ensure that your dataset is in CSV format and that the required columns are present. Replace the file_path variable with the correct path to your dataset.

Run the script:

Execute the Python script using the following command:

bash
Copy code
python <script_name>.py
The script will:

Load the dataset from the specified file path.
Handle missing values by filling them with the mean of the respective columns.
Normalize the data using StandardScaler to ensure accurate K-Means clustering.
Apply K-Means Clustering to group users based on their network experience metrics.
Calculate the experience score for each user by computing the Euclidean distance to the worst-performing cluster's centroid.
Display the MSISDN/Number and experience_score for the first few records.
Output:

The script will print the MSISDN/Number and their corresponding experience scores to the console.
The experience scores will also be saved to a CSV file named experience_scores.csv at the specified output path.
Save Results:

The script saves the output data, which includes each user's MSISDN/Number and their computed experience_score, in a CSV file for further analysis.
Key Components
Data Preprocessing:

The script handles missing values by replacing them with the column mean for the experience-related metrics.
Columns used for clustering:
Avg RTT DL (ms)
Avg RTT UL (ms)
Avg Bearer TP DL (kbps)
Avg Bearer TP UL (kbps)
TCP DL Retrans. Vol (Bytes)
TCP UL Retrans. Vol (Bytes)
Data Scaling:

The script scales the input features using StandardScaler to normalize the data, ensuring that K-Means clustering is effective.
K-Means Clustering:

The dataset is clustered into 3 groups using K-Means, based on the network experience metrics.
The cluster centroids represent the average values of each feature in each cluster.
Experience Score Calculation:

The experience score is computed for each user based on their Euclidean distance from the worst-performing cluster's centroid. A higher score indicates worse network performance relative to the worst cluster.
The worst-performing cluster is assumed to have the highest average RTT and retransmission volumes, which are key indicators of poor network experience.
Customization
Number of Clusters: You can modify the number of clusters by changing the n_clusters parameter in the K-Means model:

python
Copy code
kmeans = KMeans(n_clusters=4, random_state=42)
File Paths: You should update the file_path variable to point to your dataset, and optionally modify the output file path:

python
Copy code
file_path = 'your_input_path.csv'
output_path = 'your_output_path.csv'
Feature Columns: If you want to use a different set of features, modify the experience_columns list to include your desired columns:

python
Copy code
experience_columns = ['your_column_1', 'your_column_2', ...]
Files
script_name.py: The main Python script that handles data preprocessing, clustering, and experience score calculation.
experience_scores.csv: The output CSV file that includes the MSISDN/Number and their calculated experience scores.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
