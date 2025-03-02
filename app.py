# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify
from flask_cors import CORS

# Database Setup
engine = create_engine("sqlite:///oil_price_interest_db.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to each table using correct case
crude_oil_prices = Base.classes.crude_oil_prices  # Corrected the class name
cad_rates = Base.classes.CadRates
fed_rates = Base.classes.FedRates

# Create our session (link) from Python to the DB
session = Session(bind=engine)

# Flask Setup
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return """Welcome to the Oil Price and Interest Rates API! Use the following endpoints:<br>
           <ul>
           <li>/api/v1.0/crude_oil</li>
           <li>/api/v1.0/cad_rates</li>
           <li>/api/v1.0/fed_rates</li>
           </ul>"""

@app.route("/api/v1.0/crude_oil")
def crude_oil():
    """Return crude oil price."""
    results = session.query(crude_oil_prices).all()
    crude_oil_price_data = [
        {"year": row.Year, "month": row.Month, "WTI": row.WTI, "WCS": row.WCS} 
        for row in results
    ]
    return jsonify(crude_oil_price_data)

@app.route("/api/v1.0/cad_rates")
def get_cad_rates():
    """Return interest rates and inflation rates in Canada."""
    results = session.query(cad_rates).all()
    cad_rate = [
        {"year": row.Year, "month": row.Month, "inflation": row.Inflation, 
         "10-Year-bond": row.Ten_Year_Bond_Yield, "overnight_rate": row.Overnight_Rate} 
        for row in results
    ]
    return jsonify(cad_rate)

@app.route("/api/v1.0/fed_rates")
def get_fed_rates():
    """Return interest rates and inflation rates in the US."""
    results = session.query(fed_rates).all()
    fed_rate = [
        {"year": row.Year, "month": row.Month, "inflation": row.Inflation, 
         "10-Year-bond": row.Ten_Year_Bond_Yield, "federal_rate": row.Federal_Rate} 
        for row in results
    ]
    return jsonify(fed_rate)

if __name__ == "__main__":
    app.run(debug=True)  