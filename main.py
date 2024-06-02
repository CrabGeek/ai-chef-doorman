import nats
import asyncio


async def run():
    nc = await nats.connect(servers=["nats://localhost:4222"])

    await nc.subscribe("foo", cb=message_handler)



async def message_handler(msg):
    subject = msg.subject
    reply = msg.reply
    data = msg.data.decode()
    print(
        "Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data
        )
    )


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run())
    loop.run_forever()
