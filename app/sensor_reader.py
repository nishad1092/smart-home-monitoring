# app/main.py
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/data", methods=["GET"])
def get_sensor_data():
    df = pd.read_csv("./sensor-data.csv")
    data = df.tail(50).to_dict(orient="records")  # Last 50 records
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)