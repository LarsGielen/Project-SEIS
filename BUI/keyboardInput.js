var inputSocket = null;

window.addEventListener('load', (event) => {    
    inputServerInput = document.querySelector("#inputServerURLInput")

    document.querySelector("#URLOkButton").addEventListener('click', (event) => setupInputConnection(inputServerInput.value));
});

function setupInputConnection(url) {
    inputSocket = new WebSocket('ws://' + url);
    inputSocket.onopen = (event) => { console.log('connected to input server')};
}

let keyStatus = {
    'forward': false,
    'left': false,
    'backward': false,
    'right': false
};

function handleKeyPress(key) {
    toggleButton(key);
    publishKey();
}

document.addEventListener('keydown', function(event) {
    if (event.repeat) return;

    const key = event.key.toUpperCase();
    if (['Z', 'Q', 'S', 'D'].includes(key) && !keyStatus[key]) {
        keyStatus[getKeyName(key)] = true;
        handleKeyPress(getKeyName(key));
    }
});

document.addEventListener('keyup', function(event) {
    const key = event.key.toUpperCase();
    if (['Z', 'Q', 'S', 'D'].includes(key) && keyStatus[getKeyName(key)]) {
        keyStatus[getKeyName(key)] = false;
        handleKeyPress(getKeyName(key));
    }
});

function toggleButton(key) {
    const button = document.getElementById(key.toLowerCase() + '-btn');
    button.disabled = !keyStatus[key];
}

function publishKey() {
    let vector = { x: 0, y: 0 };

    if (keyStatus['forward']) {
        vector.y = 1;
    } else if (keyStatus['backward']) {
        vector.y = -1;
    }

    if (keyStatus['left']) {
        vector.x = -1;
    } else if (keyStatus['right']) {
        vector.x = 1;
    }
    var size = Math.sqrt(vector.x * vector.x + vector.y * vector.y);
    if (size === 0) {
        size = 1;
    }
    const normVector = { x: vector.x / size, y: vector.y / size };
    const timestamp = Date.now()
    const jsonMessage = JSON.stringify({
        type: "INPUT",
        data: {normVector, timestamp}
    });

    console.log(inputSocket.readyState == WebSocket.OPEN);
    inputSocket.send(jsonMessage);
}

function getKeyName(key) {
    switch (key) {
        case "Z":
            return "forward"
        case "Q":
            return "left"
        case "S":
            return "backward"
        case "D":
            return "right"
    }
}

window.addEventListener('load', (event) => {
    toggleButton("forward")
    toggleButton("backward")
    toggleButton("left")
    toggleButton("right")
});