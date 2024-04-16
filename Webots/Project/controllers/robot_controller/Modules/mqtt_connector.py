import paho.mqtt.client as paho
import json

class MQTTConnector():
    _BROKER = "19dec47c4ea94f028a9fb739c51578c2.s1.eu.hivemq.cloud"
    _PORT = 8883
    
    def __init__(self):
        self.client = paho.Client()
        self.client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)
        self.client.username_pw_set("Robot", "Robot123")

        self.client.connect(
            host=self._BROKER,
            port=self._PORT,
            clean_start=paho.MQTT_CLEAN_START_FIRST_ONLY,
            keepalive=60
        )

        self.client.loop_start()

    def publish(self, topic, data):
        payload = json.dumps(data)
        self.client.publish(topic, payload)

    def disconnect(self):
        self.client.disconnect()
        self.client.loop_stop()