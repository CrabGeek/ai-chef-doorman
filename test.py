import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="hotspyder_to_doorman")
    channel.queue_declare(queue="foo")

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode('utf-8')}")

    def callback_foo(ch, method, properties, body):
        print(f"Fooooooo {body}")

    channel.basic_consume(queue="hotspyder_to_doorman", on_message_callback=callback, auto_ack=True)

    channel.basic_consume(queue="foo", on_message_callback=callback_foo, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
