function solve(start, end) {
    let array = [];
    let total = 0;
    for (i=start; i<=end; i++) {
        array.push(i)
        total = total + i
    }
    console.log(array.join(" "));
    console.log(`Sum: ${total}`)
}

solve(50, 60)