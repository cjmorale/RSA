from flask import Flask, request, jsonify
from RSA.encryption import *
import json
import werkzeug.datastructures

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/create_key", methods = ['POST'])
def create_key():
    data = request.json

    length_p = data['length_p']
    length_q = data['length_q']
    length_e = data['length_e']

    rsa = RSA(length_p, length_q, length_e)

    values = rsa.generate_key()
    print(values)
    return json.dumps(rsa.generate_key())


@app.route("/encrypt", methods = ['POST'])
def encrypt():
    data = request.json

    messege = data['messege']

    p, q, e, N, d =  data['p'], data['q'], data['e'], data['N'], data['d']

    rsa = RSA(p=p, q=q, e=e, N=N, d=d)
    encrypted = rsa.encrypt(messege)

    return jsonify(encrypted)


@app.route("/decrypt", methods = ['POST'])
def decrypt():
    data = request.json
    encrypted = data['encrypted']
    p, q, e, N, d = data['p'], data['q'], data['e'], data['N'], data['d']
    rsa = RSA(p=p, q=q, e=e, N=N, d=d)
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
    app.run(debug=True, host = '0.0.0.0', port=8080)