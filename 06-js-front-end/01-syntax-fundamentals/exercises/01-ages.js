function solve(age) {
    let result;
    if (age < 0) {
        result = 'out of bounds'
    } else if (age < 3) {
        result = 'baby'
    } else if (age < 14) {
        result = 'child'
    } else if (age < 20) {
        result = 'teenager'
    } else if (age < 66)  {
        result = 'adult'
    } else if (age >= 66) {
        result = 'elder'
    }
    console.log(result)
}

solve(0)