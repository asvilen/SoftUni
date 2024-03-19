function solve(inputList) {
    const resultsObj = {}
    const [wordsToLookFor, words] = [inputList[0].split(" "), inputList.slice(1)]
    for (const wordToLookFor of wordsToLookFor) {
        resultsObj[wordToLookFor] = 0
        for (const word of words) {
            if (wordToLookFor === word) {
                resultsObj[word] += 1
            }
        }
    }
    const sortedResultsObj = Object.fromEntries(
        Object.entries(resultsObj).sort(([, a], [, b]) => b - a)
    )
    for (const word in sortedResultsObj) {
        console.log(`${word} - ${sortedResultsObj[word]}`);
    }
}

solve([
    'this sentence', 
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ])