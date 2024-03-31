function extract(content) {
    const text = document.getElementById(content).textContent;
    const regexPattern = /\(([a-zA-z ]+)\)/g;
    const matches = text.match(regexPattern)
    let result = []
    for (const match of matches) {
        result.push(match.slice(1, -1))
    }
    return result.join("; ")
}