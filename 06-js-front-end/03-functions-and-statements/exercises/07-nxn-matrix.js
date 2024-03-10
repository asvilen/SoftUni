function printMatrix(size) {
    const arrayToPush = Array(size).fill(size);
    let result = [];
    for (i = 0; i < size; i++) {
        result.push(arrayToPush)
    }
    result.forEach(row => {
        console.log(...row);
    });
}

printMatrix(7)