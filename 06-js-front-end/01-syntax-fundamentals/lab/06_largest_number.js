function solve(num1, num2, num3) {
    let largest = - Number.MAX_VALUE
    if (largest < num1) {
        largest = num1;
    }
    if (largest < num2) {
        largest = num2;
    }
    if (largest < num3) {
        largest = num3;
    }
    console.log(`The largest number is ${largest}.`)
}

solve(-3, -5, -22.5)