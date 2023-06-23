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

@socketio.on('broadcast_message')
def handle_broadcast_message(data):
    message = data['message']
    print("Message -->",message)
    emit('messagesBroadcast', {'text': f'{message}'},broadcast=True)

@socketio.on('send_message')
def handle_send_message(data):
    message = data['message']
    print("Message -->",message)
    emit('message', {'text': f'{message}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7002)
    socketio.run(app)
