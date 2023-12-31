from fastapi import FastAPI, WebSocket
from starlette.middleware.cors import CORSMiddleware
# import websocket
from fastapi.responses import HTMLResponse

app = FastAPI()

# Enable CORS if necessary
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = []

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws/react");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws/react")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        # You can add more sophisticated logic here, e.g., handling different types of messages
        message = await websocket.receive_text()
        await websocket.send_text(f"Message received: {message}")

@app.websocket("/ws/robot")
async def robot_websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        print(message)
        for client in clients:
            await client.send_text(f"Message from robot: {message}")
        await websocket.send_text(f"Message received: {message}")
        
