from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('join_room')
def handle_join_room(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('message', {'text': f'{username} has joined the room.'}, room=room)

@socketio.on('send_message')
def handle_send_message(data):
    username = data['username']
    room = data['room']
    message = data['message']
    emit('message', {'text': f'{username}: {message}'}, room=room)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6002)
    socketio.run(app)
