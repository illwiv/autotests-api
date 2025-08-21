import asyncio
import websockets


async def echo(websocket):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        for i in range(5):
            await websocket.send(f"{i + 1} Сообщение пользователя: {message}")


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket server started on ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())
