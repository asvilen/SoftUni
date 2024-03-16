function solve(name, lastName, hairColor) {
    person = {
        name,
        lastName,
        hairColor
    }
    return JSON.stringify(person)
}

console.log(solve('George', 'Jones', 'Brown'));