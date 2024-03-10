function repeatString(inputString, count) {
    let result = inputString;
    for (i = 1; i < count; i++) {
        result += inputString
    }
    return result
}

console.log(repeatString("abc", 3));
console.log(repeatString("String", 2));
