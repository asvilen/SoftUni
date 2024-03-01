function solve(year) {
    let result = 'no'
    if (year % 400 === 0) {
        result = 'yes'
    } else if (year % 100 !== 0 && year % 4 === 0) {
        result = 'yes'
    }

    return result
}

console.log(solve(4));