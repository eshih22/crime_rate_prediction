from flask import Flask, send_from_directory, request, jsonify
from server import CrimePredictor

app = Flask(__name__, static_url_path='/')
app.static_folder = 'dist'


@app.route('/')
def root():
    return send_from_directory('dist', 'index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        csv = data.get('csv')
        predict = CrimePredictor.predict(data.get('algorithm'), csv)
        return jsonify(predict)
    except ZeroDivisionError:
        return jsonify({"error": "unexpected error"})


if __name__ == '__main__':
    app.run(port=8000, debug=True)
