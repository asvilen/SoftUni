function solve(inputList) {
    let addBook = {};
    for (const person of inputList) {
        const [name, address] = person.split(":")
        
        addBook[name] = address
    }
    const sortedAddBook = Object.fromEntries(Object
        .entries(addBook)
        .sort(([key, value], [keyB, valueB]) => key.localeCompare(keyB)))
    for (const name in sortedAddBook) {
        console.log(`${name} -> ${sortedAddBook[name]}`);
    }
}

solve(['Tim:Doe Crossing',
'Bill:Nelson Place',
'Peter:Carlyle Ave',
'Bill:Ornery Rd'])