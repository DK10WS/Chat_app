from fastapi import WebSocket, APIRouter

class ManageConnections():

    def __init__(self):
        self.active_connection = []

    async def connect(self,websocket:WebSocket):
        await websocket.accept()
        self.active_connection.append(websocket)
    
    def disconnect(self, websocket:WebSocket):
        self.active_connection.remove(websocket)
    
    async def send_message(self, websocket: WebSocket, message: str):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connection:
            await connection.send_text(message)

router = APIRouter() # Reuse current working ip

connection_manager = ManageConnections()

@router.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):
    await connection_manager.connect(websocket)
    try:
            while True:
                data = await websocket.receive_text()
                await connection_manager.broadcast(f"Client says: {data}")
    except Exception:
        connection_manager.disconnect(websocket)





