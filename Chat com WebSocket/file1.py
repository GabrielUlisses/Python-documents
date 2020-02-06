from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def hello():
    return open('html/index.html').read()

@socketio.on('messsage')
def messagereceived(data):
    

if __name__ == '__main__':
    socketio.run(app,'127.0.0.1',3000)
