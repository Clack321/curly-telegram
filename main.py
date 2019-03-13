from flask import Flask, render_template, request
from flask_socketio import SocketIO
import asyncio
import requests

app = Flask(__name__) #Veerrryy similar to express, but not quite
#app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app) #Veerrryy similar to express, but not quite

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('weather')
def handleWeather(json, methods=['GET', 'POST']):
    res = requests.get('https://www.metaweather.com/api/location/search/?query=north')
    resJSON = res.json()
    print(resJSON) # console log never hurt anyone
    socketio.emit('weatherResponse', resJSON, callback=messageReceived)

@socketio.on('color')
def handleColor(json, methods=['GET', 'POST']):
    socketio.emit('colorResponse', json, callback=messageReceived) #emmitting a response to the client from the server, returning mesage was recieved!!!


@socketio.on('my event') #when 'my event' event is returned from the client
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json)) # console log never hurt anyone
    socketio.emit('my response', json, callback=messageReceived) #emmitting a response to the client from the server, returning mesage was recieved!!!

if __name__ == '__main__':
    socketio.run(app, debug=True)