function solve(number) {
    let allAreTheSame = true;
    let lastNum = Number(String(number)[0]);
    let sum = 0;
    for (const num of String(number)) {
        let current_num = Number(num)
        sum += current_num
        if (lastNum !== current_num) {
            allAreTheSame = false
        }
        lastNum = current_num
    }
    console.log(allAreTheSame);
    console.log(sum);
}

solve(2222222)
