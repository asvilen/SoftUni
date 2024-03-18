function solve(inputList) {
    const resultList = []
    for (const city of inputList) {
        let [town, latitude, longitude] = city.split(" | ")
        resultList.push({
            town,
            latitude: Number(latitude).toFixed(2),
            longitude: Number(longitude).toFixed(2),
        })
    }
    for (const town of resultList) {
        console.log(town);
    }
}

solve(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625'])