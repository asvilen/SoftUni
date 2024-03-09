function solve(inputString) {
    let inputStringList = inputString.split(" ");
    for (let word of inputStringList) {
        if (word.startsWith("#") && word.length > 1) {
            word = word.slice(1)
            if (! word.match(/\d/)) {
                console.log(word);
            }
            

        }
    }
}

// solve('Nowadays everyone uses # to tag a #special word in #socialMedia')
solve('The symbol # is known #various3ly in English-speaking #regions as the #number sign')