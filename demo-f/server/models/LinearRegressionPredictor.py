import joblib
import os
from pathlib import Path

base_dir = os.path.dirname(os.path.abspath(__file__))
crime_prediction_file = os.path.join(base_dir, "./files/linear_regression_model.pkl")
crime_prediction_model = joblib.load(crime_prediction_file)


def predict(data):
    prediction = crime_prediction_model.predict(data)
    return prediction[0]
