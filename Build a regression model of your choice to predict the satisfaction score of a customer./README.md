Satisfaction Score Prediction
This project aims to predict the satisfaction score of users based on various features such as network performance metrics, engagement score, and experience score. The script includes data preprocessing, model training, evaluation, and visualization of results using both Linear Regression and Random Forest models.

Table of Contents
Installation
Dataset
Features
Target Variable
Models Used
Evaluation Metrics
Visualization
Usage
Results
License
Installation
To run this script, you'll need to have Python installed along with the following libraries:

bash
Copy code
pip install pandas numpy scikit-learn matplotlib
Dataset
The dataset should be in CSV format and should contain computed columns such as engagement_score, experience_score, and satisfaction_score, along with other network performance metrics. You can modify the file path to your dataset in the script:

python
Copy code
file_path = 'D:/10 Acadamy kifiya/Technical Content/data/Week1_challenge_data_source(CSV)'
Features
The following features are used to predict the satisfaction score:

Avg RTT DL (ms)
Avg RTT UL (ms)
Avg Bearer TP DL (kbps)
Avg Bearer TP UL (kbps)
TCP DL Retrans. Vol (Bytes)
TCP UL Retrans. Vol (Bytes)
engagement_score
experience_score
Target Variable
satisfaction_score: This is the dependent variable that the model will predict based on the features listed above.
Models Used
Linear Regression: A basic regression model to predict the satisfaction score.
Random Forest Regressor (optional): Another model that can be used by uncommenting the corresponding lines of code in the script. It may provide better accuracy due to its ability to handle non-linear relationships.
Evaluation Metrics
Two evaluation metrics are used to assess the performance of the model:

Mean Squared Error (MSE): Measures the average squared difference between the actual and predicted values.
R² Score: Measures how well the predictions approximate the actual data.
Visualization
A scatter plot is generated to compare actual vs. predicted satisfaction scores for the Linear Regression model.

Usage
Load the dataset by updating the file_path variable with your CSV file's path.
Make sure the dataset has computed values for engagement_score, experience_score, and satisfaction_score.
Select a regression model (Linear Regression or Random Forest).
The script will train the model on 80% of the dataset and test it on the remaining 20%.
Predictions and evaluation metrics will be displayed in the console.
A scatter plot comparing actual and predicted satisfaction scores will be generated.
Optionally, you can save the prediction results to a CSV file by providing a path.
Example:
bash
Copy code
python satisfaction_prediction.py
Results
Linear Regression:
Mean Squared Error (MSE)
R² Score
Random Forest Regressor (optional):
Mean Squared Error (MSE)
R² Score
License
This project is open-source and available for modification and use.
