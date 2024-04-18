window.addEventListener('load', (event) => {
    radarElement = document.querySelector('#radarplot')
    
    function onMessage(event) {
        addRadarPoint(JSON.parse(event.data))
    }
    
    const socket = new WebSocket('ws://localhost:5001');
    socket.onopen = (event) => { console.log('connected to radar stream')};
    socket.onmessage = onMessage;

    function addRadarPoint(data) {
        const radarPlot = document.getElementById('radarplot');
        var max_length = 3;

        while (radarPlot.firstChild) {
            radarPlot.removeChild(radarPlot.lastChild);
        }

        data.forEach(point => {
            point.x = (point.x / max_length) / 2 + 0.5;
            point.y = (point.y / max_length) / 2 + 0.5;

            const radarPoint = document.createElement('div');
            radarPoint.className = 'radarPoint';
            radarPoint.style.setProperty('--x', point.x);
            radarPoint.style.setProperty('--y', point.y);
            radarPlot.appendChild(radarPoint);
        });
    }

});