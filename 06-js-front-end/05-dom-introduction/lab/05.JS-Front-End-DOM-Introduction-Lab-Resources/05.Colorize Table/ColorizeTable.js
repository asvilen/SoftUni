function colorize() {
    const evenTableRows = document.querySelectorAll('table tr:nth-child(2n)')

    for (const row of evenTableRows) {
        row.style.backgroundColor = 'teal'
    }
}