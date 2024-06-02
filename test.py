
import nats
import asyncio


async def run():
    nc = await nats.connect(servers=["nats://localhost:4222"])

    for i in range(0, 10):
        data = f'Hello-{i}'
        await nc.publish("foo", str.encode(data))


if __name__ == '__main__':
    asyncio.run(run())