function minOfThree(numOne, numTwo, numThree) {
    return [numOne, numTwo, numThree].sort((a, b) => a - b)[0]
}

console.log(minOfThree(-1, 5, 134));
console.log(minOfThree(600, 342, 923));
console.log(minOfThree(2, 14, 2));