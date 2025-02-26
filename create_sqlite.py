import sqlite3
import pandas as pd
from pathlib import Path

# Create a new SQLite database 
database_path = "oil_price_interest_db.sqlite"
conn = sqlite3.connect(database_path)
c = conn.cursor()

# Create the table for crude oil price
c.execute('''
CREATE TABLE IF NOT EXISTS crude_oil_prices (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,        
    Year INT NOT NULL,
    Month INT NOT NULL,                          
    WTI DECIMAL(20, 10), 
    WCS DECIMAL(20, 5)
)
''')

# Create table for Canadian Rates
c.execute('''
CREATE TABLE IF NOT EXISTS CadRates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Year INT NOT NULL,
    Month INT NOT NULL,
    Inflation DECIMAL(20, 5),
    Ten_Year_Bond_Yield DECIMAL(20, 5),
    Overnight_Rate DECIMAL(20, 5)
)
''')

# Create table for Federal Rates
c.execute('''
CREATE TABLE IF NOT EXISTS FedRates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Year INT NOT NULL,
    Month INT NOT NULL,
    Inflation DECIMAL(20, 5),
    Ten_Year_Bond_Yield DECIMAL(20, 5),
    Federal_Rate DECIMAL(20, 5)
)
''')

# Commit changes to the database
conn.commit()

# Define paths to CSV files
csv_files = {
    'crude_oil_prices': '/Users/junjiang/project_4_oil_price_prediction/Cleaned_Data/df_crude_oil.csv',
    'CadRates': '/Users/junjiang/project_4_oil_price_prediction/Cleaned_Data/cad_rates.csv',
    'FedRates': '/Users/junjiang/project_4_oil_price_prediction/Cleaned_Data/fed_rates.csv'
}

for table_name, csv_file in csv_files.items():
   df =pd.read_csv(csv_file)
    # Import the DataFrame into the SQLite table
   df.to_sql(table_name, conn, if_exists='append', index=False)

# Close the connection
conn.close()

