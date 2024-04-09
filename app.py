from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')  # Load your trained Random Forest model

@app.route('/')
def home():
    return "Random Forest Model API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run(debug=True)