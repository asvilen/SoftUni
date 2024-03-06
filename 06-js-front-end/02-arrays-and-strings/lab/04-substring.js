function solve(string, num1, num2) {
    // let result = ''; // = string.slice(num1, num2 + 1)
    let result = string.substring(num1, num1 + num2);
    // for (let i = num1; i <= num2; i++) {
    //     result += string[i]
    // }
    console.log(result);
}

solve('ASentence', 1, 8)
solve('SkipWord', 4, 7)