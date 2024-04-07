function generateReport() {
    const theadElement = document.querySelectorAll('thead tr th')
    const tableRows = document.querySelectorAll('tbody tr')
    const outputElement = document.getElementById('output')

    const columns = Array
        .from(theadElement)
        .map(th => {
            const checkbox = th.querySelector('input[type=checkbox]')
            return {
                name: th.textContent.toLowerCase().trim(),
                status: checkbox.checked,
            }
        })

    const reportData = Array
        .from(tableRows)
        .map(trElement => {
            const tdElements = trElement.querySelectorAll('td')

            const result = Array
                .from(tdElements)
                .reduce((result, value, i) => {
                    const name = columns[i].name
                    const isActive = columns[i].status
                    if (isActive) {
                        result[name] = value.textContent
                        return result
                    }
                    return result
                }, {})
            return result
        })

    outputElement.value = JSON.stringify(reportData, null, 2)
}