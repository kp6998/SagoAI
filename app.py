from flask import Flask, request, jsonify
from flask_cors import CORS
from API_Response import CallAPI

app = Flask(__name__)
CORS(app)

@app.route('/my_api_endpoint')
def my_api_function():
    txtInput = "Remember, you are name as Sago, personal assistant chatbot for Prakash.\
    I need you to reply the people who are visiting prakash.vip website.\
    Now reply to this - "
    param = request.args.get('param')
    result = CallAPI(txtInput+param)
    #response = {'result': 'success'}
    return jsonify(result)

if __name__ == '__main__':
    app.run()
