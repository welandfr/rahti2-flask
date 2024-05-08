import os
from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()

PORT = os.environ.get('PORT', 8080)

app = Flask(__name__)

with app.app_context():
    # Init code here
    print(f'Flask app running on port {PORT}')

@app.route("/")
def index():
    print(f'{request.method} request from {request.remote_addr}')
    ret = {
        'msg': 'Rahti Flask demo works.', 
        'env': os.environ.get('ENV_VAR', 'not working'), 
        'method': request.method
    }

    return ret

@app.route("/test-route", methods = [ 'GET', 'POST' ])
def test_route():

    if request.method == 'POST':
    
        try:
            ret =  { 'msg': 'POST works', 'postdata': request.get_json() }

        except Exception as e:
            print(e)
            ret =  { 'msg': 'ERROR: POST failed.' }, 500

    else:
        ret = {'msg': 'Test route GET'}

    return ret

if __name__ == "__main__":
    app.run(debug=True, port=PORT, host='0.0.0.0' )
    
