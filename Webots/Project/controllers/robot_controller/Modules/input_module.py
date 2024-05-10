from websockets.server import serve
from websockets import exceptions 
from threading import Thread
import asyncio

from dataclasses import dataclass
import time
import json

@dataclass
class InputData():
    direction_forward: float
    direction_right: float
    timestamp: int

class Input():
    input_data: InputData = InputData(0, 0, 0)
    emergency_stop: bool = False
    
    def __init__(self) -> None:
        self.startServerThreaded()

    def startServerThreaded(self):
        thread = Thread(target=lambda: asyncio.run(self._startServer()))
        thread.start()

    async def _startServer(self):
        print('Input server started on port 5000\n')
        async with serve(self._handler, "0.0.0.0", 5000):
            await asyncio.Future()  # run forever

    async def _handler(self, websocket):
        try:
            while True:
                message = await websocket.recv()  
                self._on_message(message)
        except (exceptions.ConnectionClosed, exceptions.ConnectionClosedError) as e:
            print("Disconnected")
            self.input_data = InputData(0, 0, time.time()) 

    def _on_message(self, message):
        message_data = json.loads(message)

        if message_data['type'] == "INPUT":
            '''
            Input is expected in json format and to be formatted like:
            {
                'type': INPUT,
                'data': {
                    'normVector': {'x': 0, 'y': 0}, 
                    'timestamp': 1712759171228
                } 
            }
            '''
            if (self.input_data.timestamp < int(message_data['data']['timestamp'])):
                self.input_data = InputData( 
                    direction_forward=message_data['data']['normVector']['y'],
                    direction_right=message_data['data']['normVector']['x'],
                    timestamp=message_data['data']['timestamp']
                )

        if message_data['type'] == "EMERGENCY":
            '''
                Input is expected in json format and to be formatted like:
                {
                    'type': EMERGENCY,
                    'data': {
                        'emergency': False
                    }
                }
            '''
            self.emergency_stop = message_data['data']['emergency']

            if (message_data['data']['emergency'] == False):
                self.input_data = InputData(0, 0, time.time())
