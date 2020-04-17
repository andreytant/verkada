from flask import Flask, request
import threading
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hi, this is server!'

@app.route('/getMessage', methods=['GET'])
def getMessage():
    return "To be completed"

app.run(debug=True, port=4000)