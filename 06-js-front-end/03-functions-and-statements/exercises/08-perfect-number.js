function perfectCheck(number) {
    let divisorSum = 0;
    for (i = 1; i < number; i++) {
        if (number % i === 0) {
            divisorSum += i
        }
    }
    if (number === divisorSum) {
        console.log("We have a perfect number!");
    } else {
        console.log("It's not so perfect.")
    }
}

perfectCheck(6);
perfectCheck(28);
perfectCheck(1236498);