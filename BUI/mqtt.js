const client = new Paho.MQTT.Client('19dec47c4ea94f028a9fb739c51578c2.s1.eu.hivemq.cloud', Number(8884), "/mqtt", 'client-id:' + Math.random().toString(16).substr(2, 8));

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
    // console.log('Message received:', message.payloadString);
}

function sendData(data) {
    var message = new Paho.MQTT.Message(data);
    message.qos = 2;
    message.destinationName = "Robot/input";
    client.send(message);
}
