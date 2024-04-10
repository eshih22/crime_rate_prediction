import pandas as pd

from sklearn.preprocessing import StandardScaler
import RandomForestPredictor


def predict(algorithm, dataset):
    dataset_df = pd.DataFrame(dataset, index=dataset.keys())
    cleanDataset_df = cleanDataset(dataset_df)
    result = {
        'prediction': 0,
        "error": None
    }
    if algorithm == 'linear-regression':
        result.prediction = LinearRegressionPredictor.predict(cleanDataset_df)
    elif algorithm == 'neural-network':
        result.prediction = NNCrimePredictor.predict(dataset_df)
    elif algorithm == 'random-forest':
        result.prediction = RandomForestPredictor.predict(cleanDataset_df)
    else:
        result.error = "Invalid Algorithm"
    return result


def cleanDataset(dataset_df):
    scaled_df = scaleData(dataset_df)
    return scaled_df


def scaleData(data):
    scaler = StandardScaler()
    model_scaler = scaler.fit(data)
    data_predict_scaled = model_scaler.transform(data)
    return data_predict_scaled
