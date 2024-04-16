window.addEventListener('load', (event) => {
    imageElement = document.querySelector('#cameraImage')
    
    function onMessage(event) {
        console.log(event.data)
        const imageURL = URL.createObjectURL(event.data);
        const image = document.createElement('image');
        imageElement.src = imageURL;
        image.onload = function() {URL.revokeObjectURL(imageURL)}
    }
    
    const socket = new WebSocket('ws://localhost:5000');
    socket.onopen = (event) => { console.log('connected to video stream')};
    socket.onmessage = onMessage;
});
