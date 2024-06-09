from chef_mq import instant
from chef_consumers import handle_message
from chef_utility import THREAD_POOL


if __name__ == '__main__':
    try:
        instant.consume(channel_name="hotspyder_to_doorman", cb=handle_message)
    except Exception as e:
        print(e)
        THREAD_POOL.shutdown()