function extractText() {
    const nodeItems = document.querySelectorAll('ul li')
    let textArea = document.getElementById('result')

    for (const node of nodeItems) {
        textArea.value += node.textContent + '\n'
    }
}