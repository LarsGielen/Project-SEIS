window.addEventListener('load', function() {
    let isEmergencyOn = false;
    const emergencyBtn = document.querySelector('#emergencyStop');

    emergencyBtn.addEventListener('click', function() {
        isEmergencyOn = !isEmergencyOn;
        const jsonMessage = JSON.stringify({ 
            type: "EMERGENCY", 
            data: {emergency: isEmergencyOn} 
        });

        inputSocket.send(jsonMessage);

        emergencyBtn.style.backgroundColor = isEmergencyOn ? 'red' : '';
        emergencyBtn.style.borderColor = isEmergencyOn ? 'red' : '';
    });
});
