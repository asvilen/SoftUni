function attachEventsListeners() {
    // times table
    const valuesMap = {
        'days': 1,
        'hours': 24,
        'minutes': 1440,
        'seconds': 86400,
    }
    // Create button elements list
    const buttonIDs = [
        'daysBtn',
        'hoursBtn',
        'minutesBtn',
        'secondsBtn',
    ]
    const buttonsElements = buttonIDs
        .map(btnID => {
            return document.getElementById(btnID)
    })
    // Create input elements list
    const inputIDs = [
        'days',
        'hours',
        'minutes',
        'seconds',
    ]
    // Create input elements obj
    inputObjs = {}
    for (const inputID of inputIDs) {
        inputObjs[inputID] = document.getElementById(inputID)
    }

    // Create listeners
    // Button clicks
    for (const buttonEl of buttonsElements) {
        buttonEl.addEventListener('click', () => {
            for (const inputID in inputObjs) {
                const inputValue = inputObjs[inputID].value
                // If you see an input
                if (inputValue) {
                    let days;
                    // If days take the value
                    if (inputID === 'days') {
                        days = inputValue
                    // Otherwise, calculate days
                    } else {
                        days = inputValue / valuesMap[inputID]
                    }
                    // update values based on days
                    for (const key in inputObjs) {
                        inputObjs[key].value = days * valuesMap[key]
                    }
                }
            }
        })
        // Refresh on input field click
        for (const key in inputObjs) {
            inputObjs[key].addEventListener('click', () => {
                for (const key in inputObjs) {
                    inputObjs[key].value = ''
                }
            })
        }
    }
}