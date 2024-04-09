function addItem() {
    const newTextElement = document.getElementById('newItemText');
    const newValueElement = document.getElementById('newItemValue');
    const selectElement = document.getElementById('menu');
    const newOptionElement = createOption(newTextElement.value, newValueElement.value);

    selectElement.appendChild(newOptionElement)

    newTextElement.value = '';
    newValueElement.value = '';

    function createOption(text, value) {
        const newOptionElement = document.createElement('option');
        newOptionElement.textContent = text;
        newOptionElement.value = value;
        return newOptionElement
    }
}