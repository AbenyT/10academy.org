User Engagement Data Export to MySQL
This project demonstrates how to import a dataset with user engagement, experience, and satisfaction scores into a MySQL database using Python.

Table of Contents
Installation
MySQL Setup
Python Script Overview
Usage
License
Installation
Step 1: Install MySQL Connector for Python
To interact with a MySQL database from Python, you need to install the mysql-connector-python library.

bash
Copy code
pip install mysql-connector-python
Step 2: Other Required Libraries
Ensure you also have pandas installed for handling CSV data:

bash
Copy code
pip install pandas
MySQL Setup
Step 1: Create a Database
In MySQL, create a database named user_scores:

sql
Copy code
CREATE DATABASE user_scores;
Step 2: Create a Table
Switch to the user_scores database and create a table to store user engagement, experience, and satisfaction scores:

sql
Copy code
USE user_scores;

CREATE TABLE user_engagement (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    engagement_score FLOAT,
    experience_score FLOAT,
    satisfaction_score FLOAT
);
This table will hold the following columns:

user_id: A unique identifier for each user (auto-incrementing).
engagement_score: The engagement score for each user.
experience_score: The experience score for each user.
satisfaction_score: The satisfaction score for each user.
Python Script Overview
The provided Python script performs the following tasks:

Loads the dataset containing the computed engagement, experience, and satisfaction scores.
Connects to the MySQL database.
Inserts the data from the CSV file into the MySQL table.
Closes the connection once the data insertion is complete.
Database Connection
python
Copy code
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="user_scores"
)
Make sure to replace:

host: Your MySQL server's host (e.g., localhost).
user: Your MySQL username (default is root).
password: Your MySQL password.
database: The name of the database (user_scores).
Data Insertion
The script iterates over each row of the data and inserts the values into the user_engagement table using SQL INSERT statements.

python
Copy code
sql = "INSERT INTO user_engagement (engagement_score, experience_score, satisfaction_score) VALUES (%s, %s, %s)"
Each row of the dataset is inserted into the MySQL table.

Usage
Prepare the Dataset: Ensure your dataset has the following columns:

engagement_score
experience_score
satisfaction_score
Load your dataset using the pandas library:

python
Copy code
file_path = 'D:/10 Acadamy kifiya/Technical Content/data/Week1_challenge_data_source(CSV)'
data = pd.read_csv(file_path)
Run the Python Script: After configuring your MySQL credentials in the script, run the script to load the data into the MySQL database:

bash
Copy code
python export_to_mysql.py
Verify the Data: After running the script, you can verify that the data has been successfully inserted into the user_engagement table:

sql
Copy code
SELECT * FROM user_engagement;
License
This project is open-source and available for modification.

