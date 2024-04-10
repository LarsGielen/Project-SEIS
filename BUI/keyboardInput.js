let keyStatus = {
    'Z': false,
    'Q': false,
    'S': false,
    'D': false
};

function handleKeyPress(key) {
    toggleButton(key);
    publishKey(key);
}

document.addEventListener('keydown', function(event) {
    const key = event.key.toUpperCase();
    if (['Z', 'Q', 'S', 'D'].includes(key) && !keyStatus[key]) {
        keyStatus[key] = true;
        handleKeyPress(key);
    }
});

document.addEventListener('keyup', function(event) {
    const key = event.key.toUpperCase();
    if (['Z', 'Q', 'S', 'D'].includes(key) && keyStatus[key]) {
        keyStatus[key] = false;
        handleKeyPress(key);
    }
});

function toggleButton(key) {
    const button = document.getElementById(key.toLowerCase() + '-btn');
    button.disabled = !keyStatus[key];
}

function publishKey(key) {
    let vector = { x: 0, y: 0 };

    if (keyStatus['Z']) {
        vector.y = 1;
    } else if (keyStatus['S']) {
        vector.y = -1;
    }

    if (keyStatus['Q']) {
        vector.x = -1;
    } else if (keyStatus['D']) {
        vector.x = 1;
    }
    var size = Math.sqrt(vector.x * vector.x + vector.y * vector.y);
    if (size === 0) {
        size = 1;
    }
    const normVector = { x: vector.x / size, y: vector.y / size };
    const timestamp = Date.now()
    const jsonMessage = JSON.stringify({normVector, timestamp});
    sendData(jsonMessage);
}