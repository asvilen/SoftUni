function solve(cityString) {
    cityObj = JSON.parse(cityString);
    for (const key in cityObj) {
        console.log(`${key}: ${cityObj[key]}`);
    }
}

solve('{"name": "George", "age": 40, "town": "Sofia"}')