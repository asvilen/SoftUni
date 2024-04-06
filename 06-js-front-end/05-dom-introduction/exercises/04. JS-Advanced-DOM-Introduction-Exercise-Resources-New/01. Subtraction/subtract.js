function subtract() {
    const firstNumber = document.getElementById("firstNumber").value;
    const secondNumber = document.getElementById("secondNumber").value;
    const resultElement = document.getElementById("result");

    let product = Number(firstNumber) - Number(secondNumber)

    resultElement.textContent = product;
}
