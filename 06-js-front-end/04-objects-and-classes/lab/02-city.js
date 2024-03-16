function solve(cityObj) {
    for (const key in cityObj) {
        console.log(`${key} -> ${cityObj[key]}`);
    }
}


solve({
    name: "Sofia",
    area: 492,
    population: 1238438,
    country: "Bulgaria",
    postCode: "1000"
}
)