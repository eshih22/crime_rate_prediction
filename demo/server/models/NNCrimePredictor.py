import os
from pathlib import Path
from tensorflow.keras.models import load_model

base_dir = os.path.dirname(os.path.abspath(__file__))
crime_prediction_file = os.path.join(base_dir, "./files/NN.keras")
crime_prediction_model = load_model(crime_prediction_file)


def predict(data):
    predictions = crime_prediction_model.predict(data)
    if predictions.ndim != 1:
        predictions = predictions.flatten()
    return predictions
