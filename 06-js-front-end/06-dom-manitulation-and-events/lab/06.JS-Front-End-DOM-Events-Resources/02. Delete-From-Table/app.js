function deleteByEmail() {
    const trElement = document.querySelectorAll('tbody tr');
    const resultElement = document.getElementById('result');
    const inputText = document.querySelector('input[type=text]')
    console.log(inputText.value);

    const trArray = Array
        .from(trElement)
        .map(tr => {
            return tr
        });

    let resultMsg = "Not found."
    trArray.forEach(trElement => {
        const rowData = trElement.querySelectorAll('td')
        if (rowData[1].textContent === inputText.value) {
            trElement.remove(rowData);
            resultMsg = "Deleted."
        }
    });

    resultElement.textContent = resultMsg

    inputText.value = ''

}