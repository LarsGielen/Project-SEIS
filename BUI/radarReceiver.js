window.addEventListener('load', (event) => {
    radarElement = document.querySelector('#radarplot')

    let max_radar_points = 100
    radarPoints = []

    for (let i = 0; i < max_radar_points; i++) {
        radarPoints.push(createRadarPoint())
    }

    function onMessage(event) {
        setRadarPoints(JSON.parse(event.data))
    }
    
    const socket = new WebSocket('ws://localhost:5001');
    socket.onopen = (event) => { console.log('connected to radar stream')};
    socket.onmessage = onMessage;

    function createRadarPoint() {
        const radarPoint = document.createElement('div');
        radarPoint.className = 'radarPoint';
        radarPoint.style.setProperty('--x', 2);
        radarPoint.style.setProperty('--y', 2);
        radarElement.appendChild(radarPoint);

        return radarPoint;
    }

    function setRadarPoints(data) {
        let max_range = 3;
        let skip_points_amount = Math.max(Math.ceil(data.length / max_radar_points), 1)       

        // update the positions of the points
        var counter = 0;
        for (let i = 0; i < data.length; i = i + skip_points_amount) {
            radarPoint = radarPoints[counter];
            counter++;

            pointX = data[i].y / -max_range / 2 + 0.5;
            pointY = data[i].x / -max_range / 2 + 0.5;

            radarPoint.style.setProperty('--x', pointX);
            radarPoint.style.setProperty('--y', pointY);
            
            if (data[i].collision) {
                radarPoint.style.setProperty('--color', "rgb(255, 0, 0)");
            }
            else {
                radarPoint.style.setProperty('--color', "rgb(0, 255, 0)");
            }
        }

        // Hide unused points
        while(counter < radarPoints.length) {
            radarPoint = radarPoints[counter];

            radarPoint.style.setProperty('--x', 2);
            radarPoint.style.setProperty('--y', 2);
            counter++;
        }
    }
});