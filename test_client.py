import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Connected")
    await sio.emit("join_game", {"username": "test1", "room": "ROOM1"})

@sio.event
async def join_success(data):
    print("join_success received:", data)

@sio.event
async def room_update(data):
    print("room_update received:", data)

async def main():
    await sio.connect("http://localhost:8080")
    await asyncio.sleep(2)
    await sio.disconnect()

asyncio.run(main())
