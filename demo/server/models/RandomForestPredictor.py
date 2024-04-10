import joblib
import pandas as pd
import numpy as np
import os
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor

base_dir = os.path.dirname(os.path.abspath(__file__))
crime_prediction_file = os.path.join(base_dir, "./files/random_forest.pkl")

regressor = RandomForestRegressor(n_estimators=1000)
crime_prediction_model = joblib.load(crime_prediction_file)


def predict(data_predict_scaled):
    predictions = crime_prediction_model.predict(data_predict_scaled)
    if predictions.ndim != 1:
        predictions = predictions.flatten()
    return predictions[0]
