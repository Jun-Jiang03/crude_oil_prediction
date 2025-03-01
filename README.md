# crude_oil_prediction

WSC Price Percentage Change vs GDP Model

Data Sources

Primary Data Source: SQL Database / Spark DataFrame

Dataset Used: WSC price percentage change vs GDP Model.ipynb

Main Features:

country name

country code

year

gdp_per_capita

type_

value (WSC price change)


 How to Run the Model

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

Evaluate Model Performance:

from sklearn.metrics import r2_score
y_pred = nn.predict(X_test_scaled).ravel()
r2 = r2_score(y_test, y_pred)
print(f"R² Score: {r2:.2f}")

Results & Key Findings

R² Score Achieved: >= 0.80 (meets predictive accuracy requirement)

Mean Absolute Error (MAE): Optimized below 5%

Data Source: Retrieved using SQL/Spark

Optimizations:

Used one-hot encoding for categorical variables

Applied standardization to improve training

Implemented early stopping to prevent overfitting

