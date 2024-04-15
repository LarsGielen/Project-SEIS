from dataclasses import dataclass
from Modules.mqtt_connector import MQTTConnector
import json

@dataclass
class InputData():
    direction_forward: float
    direction_right: float
    timestamp: int


class Input():
    input_data: InputData = InputData(0, 0, 0)

    def __init__(self):
        self.input_data = InputData(0, 0, 0)

        # setup client
        self.client = MQTTConnector().client

        # callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc, properties=None):
        print(f'CONNACK received with code {rc}.')
        self.client.subscribe("Robot/input")

    def on_message(self, client, userdata, message):
        '''
            Input is expected in json format and to be formatted like:

            {
                'normVector': {'x': 0, 'y': 0}, 
                'timestamp': 1712759171228
            }
        '''
        message_json_string = message.payload.decode()
        message_data = json.loads(message_json_string)
        if (self.input_data.timestamp < int(message_data['timestamp'])):
            self.input_data = InputData( 
                direction_forward=message_data['normVector']['y'],
                direction_right=message_data['normVector']['x'],
                timestamp=message_data['timestamp']
            )
        