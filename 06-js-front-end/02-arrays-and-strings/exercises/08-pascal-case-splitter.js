function solve(inputString) {
    let result = [];
    const matches = inputString.matchAll(/([A-Z][a-z]*)/g)
    for (const match of matches) {
        result.push(match[0])
    }
    console.log(result.join(", "));
}

solve('SplitMeIfYouCanHaHaYouCantOrYouCan')
solve('HoldTheDoor')
solve('ThisIsSoAnnoyingToDo')