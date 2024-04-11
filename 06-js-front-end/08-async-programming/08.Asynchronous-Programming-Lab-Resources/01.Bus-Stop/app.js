function getInfo() {
    const url = "http://localhost:3030/jsonstore/bus/businfo/";
    const stopID = document.getElementById('stopId').value;
    const stopName = document.getElementById('stopName');
    const busesUIElement = document.getElementById('buses');
    busesUIElement.textContent = ''

    fetch(url + stopID)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const busStopName = data['name'];
            const busesObj = data['buses'];

            stopName.textContent = busStopName

            for (const bus in busesObj) {
                const listElement = document.createElement('li')
                listElement.textContent = `Bus ${bus} arrives in ${busesObj[bus]} minutes`
                busesUIElement.appendChild(listElement)
            }            
        })
        .catch(stopName.textContent = "Error");
}