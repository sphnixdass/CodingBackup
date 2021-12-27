import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://127.0.0.1:3003/devtools/browser/6636d7fd-35cf-483a-9ee7-4b8e855bfcec') as websocket:

        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())
