function solve(numOne, numTwo, numThree) {
    function sum(num1, num2) {
        return num1 + num2
    }
    function subtract(sumResult, num3) {
        return sumResult - num3
    }
    return subtract(sum(numOne, numTwo), numThree)
}

console.log(solve(23, 6, 10));
console.log(solve(1, 17, 30));
console.log(solve(42, 58, 100));