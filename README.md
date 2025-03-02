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
#Dependencies
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


4. Database Setup & Data Import
Run the script to create the SQLite database and import CSV data:
python create_sqlite.py
python app.py

## Project Structure

project_4_oil_price_prediction
Resources # Raw data files (CSV)
scripts                      
    create_sqlite.py # Creates SQLite database & imports data
    app.py # Flask API for serving Interest rates and crude oil price
notebooks
    Data cleaning_oilprice_and_interest_rates.ipynb  # Jupyter notebook for data cleaning 
    Explore and training model.ipynb  # Jupyter notebook for model training

README.md #Project documentation

## Data Sources

Crude Oil Prices: WTI and WCS monthly historical prices.

Macroeconomic Indicators:
  Canadian Interest Rates (Inflation, 10-Year Bond Yield, Overnight Rate)
  US Federal Interest Rates (Inflation, 10-Year Bond Yield, Federal Rate)

All data is cleaned and stored in an SQLite database for easy querying and access.

## How to Train the Model

Open the Jupyter Notebook (Explore and training model.ipynb).
Run the data preprocessing steps.
Train multiple linear regression models and compare R² scores.
Save the best-performing model.



## API Endpoints:

GET /api/v1.0/cad_rates → Returns Canadian macroeconomic data.

GET /api/v1.0/fed_rates → Returns US macroeconomic data.



## Author

Jasleen Kaur, Jun Jiang, and Anjila Ghimire
