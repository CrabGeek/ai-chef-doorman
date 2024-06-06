import pika
from pika.delivery_mode import DeliveryMode
from chef_mq import instant

def handle_message(ch, method, properties, body):
        print(f" [x] Received {body.decode('utf-8')}")


if __name__ == '__main__':
    instant.init_connections()
    instant.consume(channel_name="hotspyder_to_doorman", callback=handle_message)