function addItem() {
    const inputElement = document.getElementById('newItemText')
    if (inputElement.value) {
        const ulElement = document.getElementById('items')
        const newItemElement = document.createElement('li')


        const deleteLinkElement = document.createElement('a');
        deleteLinkElement.textContent = "[Delete]"
        deleteLinkElement.href = "#"

        newItemElement.textContent = inputElement.value
        newItemElement.appendChild(deleteLinkElement)

        // Add event listener to the delete link
        deleteLinkElement.addEventListener("click", () => {
            newItemElement.remove();
        });


        ulElement.appendChild(newItemElement)
        inputElement.value = ''
    }
}