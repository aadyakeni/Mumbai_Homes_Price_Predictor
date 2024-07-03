from flask import Flask, request, jsonify
import util
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    
    response = jsonify({
        'region':util.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_prices', methods=['GET','POST'])
def predict_home_prices():
    area = float(request.form['area'])
    region = request.form['region']
    bhk = int(request.form['bhk'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(region, area, bhk)
    })

    return response

if __name__ == '__main__':
    print("Starting Python Flask Server for Home Price Predictions...")
    util.load_asset()
    app.run()