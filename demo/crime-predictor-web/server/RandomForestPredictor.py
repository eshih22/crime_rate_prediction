import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor

crime_prediction_file = "crime_prediction.pkl"
regressor = RandomForestRegressor(n_estimators=1000)
crime_prediction_model = joblib.load(crime_prediction_file)


def predict(data_predict_scaled):
    predictions = crime_prediction_model.predict(data_predict_scaled)
    if predictions.ndim != 1:
        predictions = predictions.flatten()
    return predictions
