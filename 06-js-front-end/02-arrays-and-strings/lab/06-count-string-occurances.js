function solve(text, word) {
    let result = 0
    let textArray = text.split(' ')
    for (const el of textArray) {
        if (el === word) {
            result += 1;
        }
    }
    console.log(result);
}

solve(
    'This is a word and it also is a sentence',
    'is'
)

solve(
    'softuni is great place for learning new programming languages',
    'softuni'
)