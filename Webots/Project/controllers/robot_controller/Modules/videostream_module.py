from websockets.server import serve
from threading import Thread
from typing import Tuple
from PIL import Image
import numpy as np
import asyncio
import io

class VideoStreamServer():
    def __init__(self, camera_size: Tuple[int, int]) -> None:
        self.image_data = np.zeros(camera_size)

    def setImageData(self, image_data):
        self.image_data = image_data

    def startServerThreaded(self):
        thread = Thread(target=lambda: asyncio.run(self.startServer()))
        thread.start()

    async def _startServer(self):
        print('Video steam server started')
        async with serve(self._handler, "localhost", 5000):
            await asyncio.Future()  # run forever

    async def _handler(self, websocket):
        print("connection received!")
        while True:
            image_array = np.array(self.image_data).astype(np.uint8).reshape((720, 1280, 3))
            image = Image.fromarray(image_array)
            with io.BytesIO() as output:
                image.save(output, format="JPEG")
                binary = output.getvalue()

            await websocket.send(binary)
