function signCheck(numOne, numTwo, numThree) {
    let negativeCounter = 0
    for (const num of [numOne, numTwo, numThree]) {
        if (num < 0) {
            negativeCounter += 1
        }
    }
    if (negativeCounter % 2 === 0) {
        return 'Positive'
    }
    return 'Negative'
}

console.log(signCheck(5, 12, -15))
console.log(signCheck(-6, -12, 14))
console.log(signCheck(-5, 1, 1))