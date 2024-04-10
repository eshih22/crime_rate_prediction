import joblib
crime_prediction_file = "crime_prediction.pkl"

joblib.dump(regressor, crime_prediction_file)

def predict(data):
    return {}