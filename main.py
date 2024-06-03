import pika
from pika.delivery_mode import DeliveryMode

# connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
# channel = connection.channel()

# channel.queue_declare(queue="foo")

# channel.basic_publish(
#     exchange="",
#     routing_key="foo",
#     body="Hello World!",
#     properties=pika.BasicProperties(delivery_mode=DeliveryMode.Transient),
# )
# print(" [x] Sent 'Hello World!'")
# connection.close()


if __name__ == '__main__':
    pass