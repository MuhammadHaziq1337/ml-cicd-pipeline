from flask import Flask, request, jsonify, render_template
from app.model import predict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    try:
        data = request.get_json()
        if not data or 'features' not in data:
            return jsonify({'error': 'Invalid input data'}), 400
        
        result = predict(data['features'])
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)