from flask import Flask, request

import os
import sys

import controller

app = Flask(__name__)

def main():
    app.run(host='0.0.0.0', port=3000, debug=True)


@app.route('/create', methods=['POST'])
def create_container():
    if request.method == 'POST':
        data = json.loads(request.data)
        app_id = 'sconericles'
        controller.create_job(app_id, ['/bin/bash'], '10.11.5.6:5000/sconericles:cast')
        controller.create_service(app_id)
        return api.post(request.json)

if __name__ == '__main__':
    main() 