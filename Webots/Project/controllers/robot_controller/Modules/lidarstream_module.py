from typing import List
from Modules.perception_module import Point
from websockets.server import serve
from websockets import exceptions 
from threading import Thread
from PIL import Image
import io
import asyncio
import json


class LidarStreamServer():
    def __init__(self) -> None:
        self._lidar_json = None

    def setLidarData(self, lidar_data: List[Point]):
        self._lidar_json = json.dumps(lidar_data)

    def startServerThreaded(self):
        thread = Thread(target=lambda: asyncio.run(self._startServer()))
        thread.start()

    async def _startServer(self):
        print('Lidar steam server started')
        async with serve(self._handler, "localhost", 5001):
            await asyncio.Future()  # run forever

    async def _handler(self, websocket):
        while True:
            try:
                if self._lidar_json is not None:
                    print(self._lidar_json)
                    await websocket.send(self._lidar_json)
            except exceptions.ConnectionClosed:
                break