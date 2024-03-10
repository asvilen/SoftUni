function oddEvenSum(number) {
    const numberString = String(number).split("")
    let oddSum = 0;
    let evenSum = 0;
    numberString.forEach(numString => {
        num = Number(numString)
        if (num % 2 === 0) {
            evenSum += num
        } else {
            oddSum += num
        }
    })
    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}

oddEvenSum(1000435)
oddEvenSum(3495892137259234)