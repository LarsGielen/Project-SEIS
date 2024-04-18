window.addEventListener('load', (event) => {
    radarElement = document.querySelector('#radarplot')
    
    function onMessage(event) {
        // console.log(event.data)
        // const imageURL = URL.createObjectURL(event.data);
        // imageElement.src = imageURL;
        // image.onload = function() {URL.revokeObjectURL(imageURL)}
    }
    
    // const socket = new WebSocket('ws://localhost:5000');
    // socket.onopen = (event) => { console.log('connected to radar stream')};
    // socket.onmessage = onMessage;
});