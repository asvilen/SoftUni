function solve(number) {
    let sum = 0;
    for (const num of String(number)) {
        sum += Number(num)
    }
    console.log(sum);
}

solve(97561)