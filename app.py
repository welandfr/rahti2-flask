import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

PORT = os.environ.get('PORT', 8080)

app = Flask(__name__)

@app.route("/")
def index():
    ret = {'msg': 'Rahti Flask demo works.', 'env_var': os.environ.get('ENV_VAR') }

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
    app.run(debug=True, port=PORT, host='0.0.0.0')
    print(f'Flask app running on port {PORT}')
