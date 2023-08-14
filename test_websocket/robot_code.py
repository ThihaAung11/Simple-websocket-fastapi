# import websocket

# def send_message_to_server(server_url, message):
#     ws = websocket.WebSocket()
#     ws.connect(server_url)
#     ws.send(message)
#     ws.close()

# server_url = "ws://localhost:8000/ws/robot"
# message = "Operation Done"
# send_message_to_server(server_url, message)
import websocket

def send_message_to_server(server_url, message):
    ws = websocket.WebSocket()
    ws.connect(server_url)
    ws.send("Hello, Server")
    print(ws.recv())
    ws.close()

server_url = r"ws://localhost:8000/ws/robot"
message = "Operation Done"
send_message_to_server(server_url, message)