function solve(word, text) {
    let textList = text.split(" ")
    for (const txtWord of textList) {
        if (word.toLowerCase() === txtWord.toLowerCase()) {
            console.log(word);
            return
        }
    }
    console.log(`${word} not found!`);
}

solve('python', 'JavaScript is the best programming language')