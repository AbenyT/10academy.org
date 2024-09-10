Overview
This project demonstrates how to use MLflow for tracking machine learning experiments, specifically with a RandomForestRegressor model from Scikit-learn. The project focuses on training a regression model, logging important metrics, and tracking the parameters using MLflow.

Requirements
Python 3.x
Pip package manager
Installation
Clone this repository:

bash
Copy code
git clone <repository_url>
cd <repository_folder>
Install the required packages using pip:

bash
Copy code
pip install -r requirements.txt
If you don't have the requirements.txt file, manually install the required packages:

bash
Copy code
pip install mlflow scikit-learn pandas
Make sure you have MLflow installed. You can install it using the following command:

bash
Copy code
pip install mlflow
Dataset
This project uses a sample CSV dataset located at 'D:/10 Acadamy kifiya/Technical Content/data/Week1_challenge_data_source(CSV)'. You should replace this path with the path to your actual dataset. Ensure the dataset includes the following columns:

engagement_score
experience_score
satisfaction_score (the target variable)
How to Run the Code
Set up the dataset: Ensure that your dataset is correctly formatted and placed in the specified file path. If using a different file path, update the file_path variable in the script to reflect the correct location.

Run the script:

Run the Python script using the following command:

bash
Copy code
python <script_name>.py
The script will:

Split the dataset into training and test sets.
Train a RandomForestRegressor model.
Calculate and log metrics like Mean Squared Error (MSE).
Log the model, parameters, and artifacts to MLflow.
Monitor with MLflow UI:

After the script execution is completed, you can monitor the experiment logs by running:

bash
Copy code
mlflow ui
Then, navigate to http://localhost:5000 to view the logged parameters, metrics, and model artifacts.

MLflow Features Used
mlflow.start_run(): Starts a new MLflow run to track the experiment.
mlflow.log_param(): Logs parameters like the number of estimators (n_estimators) and maximum depth (max_depth).
mlflow.log_metric(): Logs the model's performance metrics like Mean Squared Error (mse).
mlflow.sklearn.log_model(): Logs the trained Scikit-learn model to MLflow.
mlflow.log_artifact(): Logs output artifacts like the predictions CSV file.
Files
script_name.py: The main Python script that handles model training and MLflow tracking.
output_predictions.csv: The CSV file containing the actual and predicted values from the test set, logged as an artifact.
Customization
You can adjust the RandomForestRegressor parameters (n_estimators, max_depth, etc.) to suit your needs.
Replace the dataset path with your own data for different experiments.
License
This project is licensed under the MIT License. See the LICENSE file for details.
