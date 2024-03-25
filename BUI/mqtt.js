const client = new Paho.MQTT.Client('74a64f22a34a4978b44bb41303d40ba0.s1.eu.hivemq.cloud', Number(8884), "/mqtt", 'client-id');

client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

client.connect({
	onSuccess: onConnect, 
	userName : "VinzRoosen",
	password : "cnVlz@QoG2vTTvyO",
    useSSL: true
});

function onConnect() {
    console.log('Connected to MQTT broker');
    client.subscribe("input");
}

function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
        console.log('Connection lost:', responseObject.errorMessage);
    }
}

function onMessageArrived(message) {
    console.log('Message received:', message.payloadString);
}

function publishKey(key) {
    const message = new Paho.MQTT.Message(key);
    message.destinationName = "input";
    client.send(message);
}
