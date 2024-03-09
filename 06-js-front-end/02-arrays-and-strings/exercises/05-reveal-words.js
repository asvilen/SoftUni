function solve(words, template) {
    let wordsList = words.split(", ");
    let templWords = template.split(" ");
    let result = [];
    templWords.forEach(word => {
        if (word.includes("*")) {
            for (const wordToUse of wordsList) {
                if (wordToUse.length === word.length) {
                    word = wordToUse
                }
            }
        }
        result.push(word);
    });
    console.log(...result);
}

solve('great, learning', 'softuni is ***** place for ******** new programming languages')