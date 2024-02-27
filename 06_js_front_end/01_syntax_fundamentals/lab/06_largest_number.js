function solve(num1, num2, num3) {
    let largest = - Number.MIN_VALUE
    if (largest < num1) {
        largest = num1;
    }
    if (largest < num2) {
        largest = num2;
    }
    if (largest < num3) {
        largest = num3;
    }
    console.log(`THe largest number is ${largest}.`)
}

solve(5, -3, 16)