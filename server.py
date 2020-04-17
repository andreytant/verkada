from flask import Flask, request
import timeout_decorator
import threading
app = Flask(__name__)

# you can use this class to save state if desired
class ServerContext:
    def __init__(self):
        self.msg = None

    def receive_msg_from_client(self, msg):
        self.msg = msg

    def send_mgs_to_camera(self):
        self.msg = None

    def get_msg(self):
        return self.msg

msg_available = threading.Event()
server_context = ServerContext()

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hi, this is server!'

#Cameral waits for the message
@app.route('/getMessage', methods=['GET'])
def getMessage():
    timeout = request.args.get('timeout',default = 2)
    msg_available.wait(int(timeout))
    msg_available.clear()
    msg = server_context.get_msg()
    server_context.send_mgs_to_camera()
    if msg is None:
        return 'Timeout. No message received'
    else:
        return msg

#Client/User sends the message
@app.route('/sendMessage', methods=['GET'])
def sendMessage():
    msg = request.args.get('message')
    server_context.receive_msg_from_client(msg)
    msg_available.set()
    return 'Server received the message: {}'.format(msg)

# this will run the server on port 5000, give it a try!
app.run(debug=True, port=5000)