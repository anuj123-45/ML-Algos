from flask import Flask, request, jsonify
import utils
app = Flask(__name__)


@app.route('/get-location-names')
def get_location_names():
    response=jsonify({
        'locations':util.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin','*')



if __name__ == "__main__":
    print("Starting Flask Server for Home Price Prediction")
    app.run()
