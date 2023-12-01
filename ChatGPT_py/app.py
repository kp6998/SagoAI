from flask import Flask, request, jsonify
from flask_cors import CORS
from API_Response import CallAPI

app = Flask(__name__)
CORS(app)

@app.route('/my_api_endpoint')
def my_api_function():
    param = request.args.get('param')
    result = CallAPI(param)
    #response = {'result': 'success'}
    return jsonify(result)

if __name__ == '__main__':
    app.run()