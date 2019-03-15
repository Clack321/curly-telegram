from flask import Flask, render_template, request
from flask_socketio import SocketIO
import json
import eventlet
import eventlet.wsgi
import asyncio
import requests

app = Flask(__name__) #Veerrryy similar to express, but not quite
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
# app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)
socketio = SocketIO(app) #Veerrryy similar to express, but not quite

@app.route('/')
def sessions():
    return render_template('session.html')
    # return 'Hello World!'
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('weather')
def handleWeather(jsonZipCode, methods=['GET', 'POST']):
    # # res = requests.get('https://www.metaweather.com/api/location/search/?query=north')
    # # resJSON = res.json()
    # zipCodeDict = json.load(jsonZipCode) # console log never hurt anyone
    # zipCode = zipCodeDict.get("zipCode")
    # socketio.emit('weatherResponse', zipCodeString, callback=messageReceived)

@socketio.on('slashCall')
def handleColor(json, methods=['GET', 'POST']):
    socketio.emit('slashResponse', json, callback=messageReceived) #emmitting a response to the client from the server, returning mesage was recieved!!!


@socketio.on('my event') #when 'my event' event is returned from the client
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json)) # console log never hurt anyone
    socketio.emit('my response', json, callback=messageReceived) #emmitting a response to the client from the server, returning mesage was recieved!!!

if __name__ == '__main__':
    # deploy with eventlet
    # eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
    socketio.run(app, debug=True)
    # eventlet.wsgi.server(eventlet.listen(('', 8000)), app)