import threading
from time import sleep
from flask import Flask, render_template, request
import amqpstorm
from amqpstorm import Message

app = Flask(__name__)

class RpcClient(object):
    """Asynchronous Rpc client."""

    def __init__(self, host, username, password, rpc_queue):
        self.queue = {}
        self.host = host
        self.username = username
        self.password = password
        self.channel = None
        self.connection = None
        self.callback_queue = None
        self.rpc_queue = rpc_queue
        self.open()

    def open(self):
        """Open Connection."""
        self.connection = amqpstorm.Connection(self.host, self.username, self.password)
        self.channel = self.connection.channel()
        self.channel.queue.declare(self.rpc_queue)
        result = self.channel.queue.declare(exclusive=True)
        self.callback_queue = result['queue']
        self.channel.basic.consume(self._on_response, no_ack=True, queue=self.callback_queue)
        self._create_process_thread()

    def _create_process_thread(self):
        """Create thread for consuming RPC responses."""
        thread = threading.Thread(target=self._process_data_events)
        thread.daemon = True
        thread.start()

    def _process_data_events(self):
        """Process incoming messages."""
        self.channel.start_consuming(to_tuple=False)

    def _on_response(self, message):
        """Callback to store message by correlation_id."""
        self.queue[message.correlation_id] = message.body

    def send_request(self, payload):
        """Send an RPC request."""
        message = Message.create(self.channel, payload)
        message.reply_to = self.callback_queue
        self.queue[message.correlation_id] = None
        message.publish(routing_key=self.rpc_queue)
        return message.correlation_id

    def has_response(self, correlation_id):
        """Check if a response has been received."""
        return self.queue.get(correlation_id) is not None

    def get_response(self, correlation_id):
        """Retrieve the response message."""
        return self.queue.get(correlation_id)

@app.route('/', methods=['GET', 'POST'])
def index():
    respuesta = None
    if request.method == 'POST':
        mensaje = request.form['mensaje']
        corr_id = RPC_CLIENT.send_request(mensaje)
        while not RPC_CLIENT.has_response(corr_id):
            sleep(0.1)
        respuesta = RPC_CLIENT.get_response(corr_id)
    return render_template('index.html', respuesta=respuesta)

if __name__ == '__main__':
    RPC_CLIENT = RpcClient('127.0.0.1', 'guest', 'guest', 'rpc_queue')
    app.run(debug=True)
