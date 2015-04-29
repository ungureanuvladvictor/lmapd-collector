#!/usr/bin/python
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/data', methods=['POST'])
def upload_data():
    print request.form
    return jsonify({'result': 'OK'}), 200

if __name__ == '__main__':
    app.run()
