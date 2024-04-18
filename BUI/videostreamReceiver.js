window.addEventListener('load', (event) => {
    imageElement = document.querySelector('#cameraImage')
    
    function onMessage(event) {
        const imageURL = URL.createObjectURL(event.data);
        imageElement.src = imageURL;
        imageElement.onload = function() {URL.revokeObjectURL(imageURL)}
    }
    
    const socket = new WebSocket('ws://localhost:5000');
    socket.onopen = (event) => { console.log('connected to video stream')};
    socket.onmessage = onMessage;
});
