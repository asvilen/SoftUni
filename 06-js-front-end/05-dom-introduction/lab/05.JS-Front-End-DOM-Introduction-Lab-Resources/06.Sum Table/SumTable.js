function sumTable() {
    const numElements = document.querySelectorAll('tr td:last-of-type:not(#sum)')
    let sumElement = document.getElementById('sum')
    let sum = 0
    for (const el of numElements) {
        sum += Number(el.textContent)
    }
    sumElement.textContent = sum
}