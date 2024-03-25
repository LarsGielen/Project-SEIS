const client = new Paho.MQTT.Client('74a64f22a34a4978b44bb41303d40ba0.s1.eu.hivemq.cloud', Number(8884), "/mqtt", 'client-id:' + Math.random().toString(16).substr(2, 8));

client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

client.connect({
	onSuccess: onConnect, 
	userName : "Robot",
	password : "Robot123",
    useSSL: true
});

function onConnect() {
    console.log('Connected to MQTT broker');
    client.subscribe('Robot/input');
}

function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
        console.log('Connection lost:', responseObject.errorMessage);
    }
}

function onMessageArrived(message) {
    console.log('Message received:', message.payloadString);
}

function sendData(data) {
    const message = new Paho.MQTT.Message(data);
    message.destinationName = "Robot/input";
    client.send(message);
}
