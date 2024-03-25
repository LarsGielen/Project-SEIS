let keyStatus = {
    'Z': false,
    'Q': false,
    'S': false,
    'D': false
};
let keyIntervals = {};

function handleKeyPress(key) {
    updateButtonStatus(key, true);
    toggleButton(key);
    publishKey(key);
    keyIntervals[key] = setInterval(() => {
        publishKey(key);
    }, 50);
}

function handleKeyUp(key) {
    clearInterval(keyIntervals[key]);
    updateButtonStatus(key, false);
    toggleButton(key);
}

document.addEventListener('keydown', function(event) {
    const key = event.key.toUpperCase();
    if (['Z', 'Q', 'S', 'D'].includes(key) && !keyStatus[key]) {
        handleKeyPress(key);
        keyStatus[key] = true;
    }
});

document.addEventListener('keyup', function(event) {
    const key = event.key.toUpperCase();
    if (['Z', 'Q', 'S', 'D'].includes(key)) {
        handleKeyUp(key);
        keyStatus[key] = false;
    }
});

function toggleButton(key) {
    const button = document.getElementById(key.toLowerCase() + '-btn');
    if (button) {
        button.classList.toggle('active');
    }
}

function updateButtonStatus(key, isPressed) {
    const button = document.getElementById(key.toLowerCase() + '-btn');
    if (button) {
        button.disabled = !isPressed;
    }
}