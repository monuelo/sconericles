from flask import Flask, request
import json

SCONE_VAR = "SECRET TEST"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'Hello, SCONE World!'
    
    if request.method == 'POST':
        data = request.data
        data = json.loads(data)
        return data['test']
        
if __name__ == '__main__':
    app.run()

