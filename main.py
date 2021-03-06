from flask import Flask, request, jsonify
from RSA.encryption import *
import json
import werkzeug.datastructures
import os

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def health_check():
    return json.dumps(True)

@app.route("/create_key", methods = ['POST'])
def create_key():
    data = request.json

    length_p = data['length_p']
    length_q = data['length_q']
    length_e = data['length_e']

    rsa = RSA(length_p, length_q, length_e)

    values = rsa.generate_key()
    return json.dumps(values)


@app.route("/encrypt", methods = ['POST'])
def encrypt():
    data = request.json

    message = data['message']
    e, N =  data['e'], data['N']

    rsa = RSA(e=e, N=N)
    encrypted = rsa.encrypt(message)

    return jsonify(encrypted)


@app.route("/decrypt", methods = ['POST'])
def decrypt():
    data = request.json
    encrypted = data['encrypted']
    N, d =  data['N'], data['d']
    rsa = RSA(N=N, d=d)
    decrypted = rsa.decrypt(encrypted)

    return jsonify(decrypted)


def main(request):
    with app.app_context():
        headers = werkzeug.datastructures.Headers()
        for key, value in request.headers.items():
            headers.add(key, value)
        with app.test_request_context(method=request.method, base_url=request.base_url, path=request.path, query_string=request.query_string, headers=headers, data=request.data):
            try:
                rv = app.preprocess_request()
                if rv is None:
                    rv = app.dispatch_request()
            except Exception as e:
                rv = app.handle_user_exception(e)
            response = app.make_response(rv)
            return app.process_response(response)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
