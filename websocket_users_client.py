import asyncio
import websockets


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        print(message)
        await websocket.send(message)

        for _ in range(5):
            result = await websocket.recv()
            print(result)


asyncio.run(client())
