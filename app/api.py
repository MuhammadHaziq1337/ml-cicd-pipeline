from flask import Flask, request, jsonify, render_template
from app.model import predict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    data = request.get_json()
    result = predict(data['features'])
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)