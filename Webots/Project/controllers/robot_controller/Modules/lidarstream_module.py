from typing import List
from Modules.perception_module import Point
from websockets.server import serve
from websockets import exceptions 
from threading import Thread
import asyncio
import json

COLLISION_WARNING_RANGE = 0.35

class LidarPointJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Point):
            return obj._dict_
        return json.JSONEncoder.default(self, obj)

class LidarStreamServer():
    def __init__(self) -> None:
        self._lidar_json = None

    def setLidarData(self, lidar_data: List[Point]):
        self._lidar_json = json.dumps([{'x':point[0], 'y':point[1], 'collision':((point[0]**2 + point[1]**2) < (COLLISION_WARNING_RANGE)**2)} for point in lidar_data])

    def startServerThreaded(self):
        thread = Thread(target=lambda: asyncio.run(self._startServer()))
        thread.start()

    async def _startServer(self):
        print('Lidar steam server started on port 5002\n')
        async with serve(self._handler, "0.0.0.0", 5002):
            await asyncio.Future()  # run forever

    async def _handler(self, websocket):
        while True:
            try:
                if self._lidar_json is not None:
                    await websocket.send(self._lidar_json)
            except exceptions.ConnectionClosed:
                break