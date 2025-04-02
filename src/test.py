import asyncio
import websockets

async def test_websocket():
    async with websockets.connect("ws://127.0.0.1:8000/ws") as ws:
        await ws.send("This is a test Respond")
        response = await ws.recv()
        print("Received:", response)

asyncio.run(test_websocket())
