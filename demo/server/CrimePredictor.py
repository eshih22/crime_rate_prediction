import pandas as pd
from sklearn.preprocessing import StandardScaler
from server.models import RandomForestPredictor
# from server.models import NNCrimePredictor
from server.models import LinearRegressionPredictor
from server import Percentages


def predict(algorithm, dataset):
    dataset_df = pd.DataFrame(dataset, index=dataset.keys())
    cleanDataset_df = cleanDataset(dataset_df, algorithm)
    result = {
        'prediction': 0,
        "error": None
    }
    if algorithm == 'linear-regression':
        result['prediction'] = LinearRegressionPredictor.predict(cleanDataset_df)
    elif algorithm == 'neural-network':
        result['prediction'] = NNCrimePredictor.predict(dataset_df)
    elif algorithm == 'random-forest':
        result['prediction'] = RandomForestPredictor.predict(cleanDataset_df)
    else:
        result.error = "Invalid Algorithm"
    return result


def cleanDataset(crime_df, algorithm):
    # Remove crime and city target from features data
    X = crime_df.copy()
    X = cleanColumns(X)
    X = Percentages.performCalculations(X)

    # if algorithm == 'neural-network':
    #     X.drop(columns=["House price mean"], axis=1, inplace=True)

    return scaleData(X)


def scaleData(data):
    scaler = StandardScaler()
    model_scaler = scaler.fit(data)
    data_predict_scaled = model_scaler.transform(data)
    return data_predict_scaled


def cleanColumns(df):
    for column in df.columns:
        df[column] = df[column].astype(float)
    return df
