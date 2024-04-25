from websockets.server import serve
from websockets import exceptions 
from threading import Thread
from PIL import Image
import io
import asyncio

class VideoStreamServer():
    def __init__(self) -> None:
        self._image_binary = None

    def setImageData(self, image_data: str):
        image = Image.frombytes('RGBA', (1280, 720), image_data, 'raw', 'BGRA').convert('RGB')
        with io.BytesIO() as output:
            image.save(output, format="JPEG")
            binary = output.getvalue()
        self._image_binary = binary

    def startServerThreaded(self):
        thread = Thread(target=lambda: asyncio.run(self._startServer()))
        thread.start()

    async def _startServer(self):
        print('Video steam server started\n')
        async with serve(self._handler, "localhost", 5000):
            await asyncio.Future()  # run forever

    async def _handler(self, websocket):
        while True:
            try:
                if self._image_binary is not None:
                    await websocket.send(self._image_binary)
            except exceptions.ConnectionClosed:
                break