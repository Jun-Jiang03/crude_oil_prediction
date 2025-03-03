# Crude Oil Price Prediction using Linear Models

## Objective: Develop the best linear regression model with the highest R² score to predict crude oil prices (WTI and WCS).

## Project Overview

This project builds a predictive model for crude oil prices, focusing on WTI (West Texas Intermediate) and WCS (Western Canadian Select) prices. The model utilizes historical macroeconomic indicators such as interest rates, bond yields, and inflation to enhance prediction accuracy.

The project consists of:

Data Collection & Storage: Extracting, cleaning, and storing macroeconomic and oil price data in an SQLite database.

Data Processing & Feature Engineering: Preparing datasets for machine learning.

Model Training & Evaluation: Developing linear models, optimizing parameters, and selecting the best model based on R² scores.

## Installation & Setup

1. Clone the Repository
git clone https://github.com/Jun-Jiang03/crude_oil_prediction.git

2. Install Dependencies
Ensure you have Python 3.8+ installed. Then, install required libraries:
python -m pip install prophet
#Dependencies:
    import requests
    import json
    import pandas 
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func
    import numpy 
    from pathlib import Path
    from sklearn.linear_model import LinearRegression
    import sklearn as 
    import matplotlib.pyplot 


## Project Structure
1. GDP impact on Crude Oil Price
2. Other Macroencominc factors on Crude Oil Price
3. Geopolitic Risk Impact on Crude oil Price


###  1.WCS and WTI vs GDP 

#### Source of Data 

Primary Data Source: SQL Database / Spark DataFrame

Dataset Used: WSC price percentage change vs GDP Model.ipynb

Main Features:

country name

country code

year

gdp_per_capita

type_

value (WSC price change)


 #### How to Run the Model

Load Data from SQL/Spark:

from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://username:password@host/dbname")
df = pd.read_sql("SELECT * FROM merged_df", con=engine)

OR, load from Spark:

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("WSC_Model").getOrCreate()
spark_df = spark.read.csv("/path/to/data.csv", header=True, inferSchema=True)
df = spark_df.toPandas()

Preprocess Data:

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

Train the Neural Network Model:

import tensorflow as tf
nn = tf.keras.models.Sequential([
    tf.keras.layers.Dense(80, activation="relu"),
    tf.keras.layers.Dense(50, activation="relu"),
    tf.keras.layers.Dense(1, activation="linear")
])
nn.compile(loss="mse", optimizer="adam", metrics=["mae"])
nn.fit(X_train_scaled, y_train, epochs=100, batch_size=16, validation_split=0.2)

#### Evaluate Model Performance:

from sklearn.metrics import r2_score
y_pred = nn.predict(X_test_scaled).ravel()
r2 = r2_score(y_test, y_pred)
print(f"R² Score: {r2:.2f}")

#### Results & Key Findings

R² Score Achieved: >= 0.80 
- after trying to Optimize two times in Spark - the WTI vs GDP and WSC vs GDP does not meet this requirement

-Tried running the model three times, first by standardization, second by changing the epohs and then applying xboost

Mean Absolute Error (MAE): Optimized below 5%

Data Source: Retrieved using SQL/Spark

### Tools used to Optimize the model:

Used one-hot encoding for categorical variables

Applied standardization to improve training

Implemented early stopping to prevent overfitting

### 2.WCS and WTI vs Interest rates and Inflation

#### Database Setup & Data Import
Run the script to create the SQLite database and import CSV data:
1)python create_sqlite.py
2)python app.py
3) Notebooks
    Data cleaning_oilprice_and_interest_rates.ipynb  # Jupyter notebook for data cleaning 
    Explore and training model_interest_rates.ipynb  # Jupyter notebook for model training

#### Data Sources

Crude Oil Prices: WTI and WCS monthly historical prices.

Macroeconomic Indicators:
  Canadian Interest Rates (Inflation, 10-Year Bond Yield, Overnight Rate)
  US Federal Interest Rates (Inflation, 10-Year Bond Yield, Federal Rate)

All data is cleaned and stored in an SQLite database for easy querying and access.

#### How to Train the Model

Open the Jupyter Notebook (Explore and training model_interest_rates.ipynb).
Run the data preprocessing steps.
Train multiple linear regression models and compare R² scores.
Save the best-performing model.



#### API Endpoints:

GET /api/v1.0/cad_rates → Returns Canadian macroeconomic data.

GET /api/v1.0/fed_rates → Returns US macroeconomic data.
Data Sources

### 3. WTI and WCS vs GRP 
#### Data Cleaning and Model Training 
1. Use the following Jupyter notebooks to clean data
  - `wti_data_cleaning.ipynb`
  - `wti_data_cleaning.ipynb`
2. Use the following Jupyter notebooks to train models with WTI and WCS data
  - `GPR_WTI_model.ipynb`
  - `GPR_WTI_model.ipynb`

#### Data Sources
1. Crude Oil Prices: WTI and WCS monthly historical prices
2. Geopolitical Risk Index



## Author

Jasleen Kaur, Jun Jiang, and Anjila Ghimire
