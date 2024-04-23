window.addEventListener('load', function() {
    let isEmergencyOn = false;
    const emergencyBtn = document.querySelector('#emergencyStop');

    emergencyBtn.addEventListener('click', function() {
        isEmergencyOn = !isEmergencyOn;
        const jsonMessage = JSON.stringify({ emergency: isEmergencyOn });
        
        sendData(jsonMessage, "Robot/emergency");

        emergencyBtn.style.backgroundColor = isEmergencyOn ? 'red' : '';
        emergencyBtn.style.borderColor = isEmergencyOn ? 'red' : '';
    });
});
