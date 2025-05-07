import amqpstorm
from amqpstorm import Message

def on_request(message):
    # Procesamos el mensaje recibido
    print(f"[Servidor RPC] Recibido: {message.body}")

    # Simulamos una respuesta (puedes agregar lógica real aquí)
    response = f"Hola, recibí tu mensaje: {message.body}"

    # Creamos el mensaje de respuesta
    response_message = Message.create(message.channel, response)
    response_message.correlation_id = message.correlation_id
    response_message.reply_to = message.reply_to
    response_message.publish(routing_key=message.reply_to)

    # Confirmamos que procesamos el mensaje
    message.ack()

def main():
    connection = amqpstorm.Connection('localhost', 'guest', 'guest')
    channel = connection.channel()
    channel.queue.declare('rpc_queue')

    print("[Servidor RPC] Esperando solicitudes...")
    channel.basic.consume(on_request, queue='rpc_queue')
    channel.start_consuming()

if __name__ == "__main__":
    main()
