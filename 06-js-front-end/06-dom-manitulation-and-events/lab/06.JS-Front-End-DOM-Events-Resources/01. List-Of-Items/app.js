function addItem() {
    const inputElement = document.getElementById('newItemText')
    const outputElement = document.getElementById('items')
    const newItemElement = document.createElement('li')
    newItemElement.textContent = inputElement.value
    
    outputElement.appendChild(newItemElement)
    inputElement.value = ''
}