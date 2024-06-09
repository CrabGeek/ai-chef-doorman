import json
from chef_ai_client import openai_client
from chef_utility import THREAD_POOL
from chef_mq import instant
import pika
from pika.delivery_mode import DeliveryMode

MIDDEL_WORDS = "这是文章内容："


def handle_message(ch, method, properties, body):
    message = body.decode("utf-8")
    jsonMessage = json.loads(message)

    promption_words = jsonMessage["prompt_words"]
    request_content = (
        promption_words + " " + MIDDEL_WORDS + jsonMessage["payload"]["content"]
    )

    print(request_content)

    def do_handle_message():
        result = ""
        for chunk in openai_client.send_request(content=request_content, stream=True):
            if chunk.choices[0].delta.content is not None:
                result += chunk.choices[0].delta.content

        jsonMessage["ai_generated_content"] = result
        instant.send(
            "doorman_to_chairman",
            payload=json.dumps(jsonMessage, ensure_ascii=False),
            properties=pika.BasicProperties(delivery_mode=DeliveryMode.Transient),
        )
        # print(request_content)

    # THREAD_POOL.submit(do_handle_message)

    # print(request_content)

    # for chuck in openai_client.send_request(content=promption_words, stream=True):
    #     print(chuck)
