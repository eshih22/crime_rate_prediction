from flask import Flask, send_from_directory, request, jsonify
from server import CrimePredictor

app = Flask(__name__, static_url_path='/')
app.static_folder = 'dist'


@app.route('/')
def root():
    return send_from_directory('dist', 'index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    return jsonify(CrimePredictor.predict(data.get('algorithm'), data.get('csv')))


if __name__ == '__main__':
    app.run(debug=True)
