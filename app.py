from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Handle real-time data synchronization
@app.route('/test')
def test_route():
    ai = "Working fine"
    return ai, 200

@socketio.on('data_change')
def handle_data_change(data):
    # Broadcast the received data to all connected clients
    emit('update_data', data, broadcast=True)

@socketio.on('new_message')
def handle_new_message(data):
    # Broadcast the new message to all connected clients
    emit('broadcast_message', data, broadcast=True)

@socketio.on('clear_messages')
def handle_clear_messages():
    # Broadcast the clear action to all connected clients
    emit('clear_all_messages', broadcast=True)

@socketio.on('clear_input')
def handle_clear_input():
    # Broadcast the clear input action to all connected clients
    emit('clear_input', broadcast=True)

if __name__ == '__main__':
    # Run the Flask server
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
