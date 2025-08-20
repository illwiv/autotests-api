import asyncio
import websockets


async def echo(websocket):
    async for message in websocket:
        print(f"Получено: {message}")
        response = f"Сервер получил: {message}"

        for _ in range(10):
            await websocket.send(response)


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket server started on ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())
