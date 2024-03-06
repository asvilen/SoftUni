function solve(array) {
    array
        .sort((a, b) => a.localeCompare(b))
        .forEach((el, idx) => {
            console.log(`${idx + 1}.${el}`);
    });
}

solve(["John", "Bob", "Christina", "Ema"])