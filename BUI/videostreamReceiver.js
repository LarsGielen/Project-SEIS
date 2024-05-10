let videoFramerate = 30;
var videoLastFrameTime = 0;

window.addEventListener('load', (event) => {
    imageElement = document.querySelector('#cameraImage')
    
    videoServerInput = document.querySelector("#videoStreamURLInput")

    document.querySelector("#URLOkButton").addEventListener('click', (event) => setupVideoStream(videoServerInput.value));
});

function setupVideoStream(url) {
    const socket = new WebSocket('ws://' + url);
    socket.onopen = (event) => { console.log('connected to video stream')};
    socket.onmessage = (event) => {
        let currentTime = Date.now();
        if (currentTime - videoLastFrameTime > (1 / videoFramerate) * 1000) {
            videoLastFrameTime = currentTime;
            const imageURL = URL.createObjectURL(event.data);
            imageElement.src = imageURL;
            imageElement.onload = function() {URL.revokeObjectURL(imageURL)}
        }
    };
}