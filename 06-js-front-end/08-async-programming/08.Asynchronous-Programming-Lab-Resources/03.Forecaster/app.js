function attachEvents() {
    const baseURL = "http://localhost:3030/jsonstore/forecaster/";
    const locationElement = document.getElementById('location');
    const getButtonElement = document.getElementById('submit');
    const location = locationElement.value;
    // Forecast elements
    const forecastDivElement = document.getElementById('forecast');
    const todayElement = document.getElementById('current');
    const upcomingElement = document.getElementById('upcoming');
    // Labels
    const todayLabelElement = document.querySelector("#current .label");
    const upcomingLabelElement = document.querySelector("#upcoming .label");

    getButtonElement.addEventListener('click', () => {
        const city = locationElement.value;
        fetch(baseURL + 'locations')
            .then(response => response.json())
            .then(data => {
                const {code} = data.find(location => location.name === city)
                return Promise.all([
                    fetch(baseURL + 'today/' + code),
                    fetch(baseURL + 'upcoming/' + code)
                ])
            })
            .then(responses => Promise.all(responses.map(re => re.json())))
            .then(([today, upcoming]) => {
                todayElement.textContent = '';
                todayElement.appendChild(todayLabelElement);
                upcomingElement.textContent = '';
                upcomingElement.appendChild(upcomingLabelElement)
                forecastDivElement.style.display = 'block';
                const todayStructure = getCurrentStructure(today, symbols);
                todayElement.appendChild(todayStructure);
                const upcomingStructure = getForecastStructure(upcoming, symbols);
                upcomingElement.appendChild(upcomingStructure);
            })
            .catch(err => console.log(err))
    })

    const symbols = {
        "Sunny"       : '☀',
        "Partly sunny": '⛅',
        "Overcast"    : '☁',
        "Rain"        : '☂',
        "Degrees"     : '°',
    }

    function getForecastStructure(upcoming, symbols) {
        const forecastArray = upcoming['forecast'];
        const mainDiv = document.createElement('div');
        mainDiv.classList.add('forecast-info');
        forecastArray.forEach(day => {
            // Upcoming span 1
            const upcomingSpan = document.createElement('span');
            upcomingSpan.classList.add('upcoming');
            // Symbol
            const symbolElement = document.createElement('span');
            symbolElement.classList.add('symbol')
            symbolElement.textContent = symbols[day['condition']];
            // Temperature
            const tempElement = document.createElement('span');
            tempElement.classList.add('forecast-data');
            console.log(day)
            tempElement.textContent = `${day['low']}${symbols['Degrees']}/${day['high']}${symbols['Degrees']}`
            // Conditions
            const condElement = document.createElement('span');
            condElement.classList.add('forecast-data');
            condElement.textContent = day['condition'];

            upcomingSpan.appendChild(symbolElement);
            upcomingSpan.appendChild(tempElement);
            upcomingSpan.appendChild(condElement);
            mainDiv.appendChild(upcomingSpan);
        });

        return mainDiv
    }

    function getCurrentStructure(today, symbols) {
        const divMain = document.createElement('div');
        divMain.classList.add('forecasts');
        const degreesSymbol = symbols['Degrees'];
        // Conditions Symbol
        const symbolSpanElement = document.createElement('span');
        symbolSpanElement.classList.add('condition');
        symbolSpanElement.classList.add('symbol');
        symbolSpanElement.textContent = symbols[today['forecast']['condition']];
        // Conditions
        const conditionsElement = document.createElement('span');
        conditionsElement.classList.add('condition');

        const cityElement = document.createElement('span');
        cityElement.classList.add('forecast-data');
        cityElement.textContent = today['name'];
        conditionsElement.appendChild(cityElement);

        const degreeElement = document.createElement('span');
        degreeElement.classList.add('forecast-data');
        const high = today['forecast']['high'];
        const low = today['forecast']['low'];
        degreeElement.textContent = `${low}${degreesSymbol}/${high}${degreesSymbol}`;
        conditionsElement.appendChild(degreeElement);

        const conditionElement = document.createElement('span');
        conditionElement.classList.add('forecast-data');
        const condition = today['forecast']['condition'];
        conditionElement.textContent = condition;
        conditionsElement.appendChild(conditionElement);

        // Appending elements
        divMain.appendChild(symbolSpanElement);
        divMain.appendChild(conditionsElement);

        return divMain
    }

}

attachEvents();