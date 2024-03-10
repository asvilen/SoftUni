function charsInRange(charOne, charTwo) {
    let result = []
    const asciiCodes = [charOne.charCodeAt(), charTwo.charCodeAt()]
    for (i = Math.min(...asciiCodes) + 1; i < Math.max(...asciiCodes); i++) {
        const char = String.fromCharCode(i)
        result.push(char)
    }
    console.log(...result);
}

charsInRange('#', ':')