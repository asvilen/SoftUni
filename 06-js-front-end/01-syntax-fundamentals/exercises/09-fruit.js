function solve(fruit, weight, price) {
    const weightKG = weight / 1000
    const neededMoney = price * weightKG
    console.log(`I need $${neededMoney.toFixed(2)} to buy ${weightKG.toFixed(2)} kilograms ${fruit}.`);
}

solve(
    'apple', 1563, 2.35
)