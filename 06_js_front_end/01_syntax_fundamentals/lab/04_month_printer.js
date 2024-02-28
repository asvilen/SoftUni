function solve(month) {
    const date = new Date()
    date.setMonth(month - 1)
    monthName = date.toLocaleString('en-US', {month: 'long'})

    if (month < 13 && month > 0) {
        console.log(monthName)
    } else {
        console.log("Error!")
    }
}

solve(22)