from dataclasses import dataclass
import paho.mqtt.client as paho
import json

@dataclass
class InputData():
    direction_forward: float
    direction_right: float
    timestamp: int


class Input():
    BROKER = "19dec47c4ea94f028a9fb739c51578c2.s1.eu.hivemq.cloud"
    PORT = 8883

    input_data: InputData = InputData(0, 0, 0)

    def __init__(self):
        self.input_data = InputData(0, 0, 0)

        # setup client
        self.client = paho.Client()
        self.client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)
        self.client.username_pw_set("Robot", "Robot123")

        # callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # connect with broker
        self.client.connect(
            host = self.BROKER, 
            port = self.PORT,
            clean_start = paho.MQTT_CLEAN_START_FIRST_ONLY,
            keepalive = 60
        )

        self.client.loop_start()

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
        