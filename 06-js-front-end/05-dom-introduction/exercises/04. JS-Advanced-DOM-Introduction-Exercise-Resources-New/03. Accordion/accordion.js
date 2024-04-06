function toggle() {
    let buttonElText = document.getElementsByClassName('button').item(0);
    const extraElement = document.getElementById('extra');

    if (buttonElText.textContent === "More") {
        extraElement.style.display = 'block';
        buttonElText.textContent = 'Less'
    } else {
        extraElement.style.display = 'none';
        buttonElText.textContent = 'More'
    }
}
