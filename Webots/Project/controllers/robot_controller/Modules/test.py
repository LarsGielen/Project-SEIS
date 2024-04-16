from websockets.sync.client import connect
from PIL import Image
import io

with connect("ws://localhost:5000") as websocket:
    try:
        binary_data = websocket.recv()
        print(binary_data)
        binary_stream = io.BytesIO(binary_data)
        image = Image.open(binary_stream)
        image.show()
    except():
        print('Connection closed')