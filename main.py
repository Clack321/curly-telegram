from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app) #Veerrryy similar to express, but not quite

@app.route('/')
def sessions():
    return render_template('session.html')

@app.route('/chat2') #http route header ex. localhost:5000/chat2
def secondSession():
    return "chat2"

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event') #when 'my event' event is returned from the client
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json)) # console log never hurt anyone
    socketio.emit('my response', json, callback=messageReceived) #emmitting a response to the client from the server, returning mesage was recieved!!!

if __name__ == '__main__':
    socketio.run(app, debug=True)