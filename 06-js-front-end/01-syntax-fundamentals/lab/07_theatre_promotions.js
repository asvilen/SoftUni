function solve(day_type, age) {
    let result;
    if (age < 0) {

    } else if (day_type == 'Weekday') {
        if (age <= 18) {
            result = 12
        } else if (age <= 64) {
            result = 18
        } else if (age <= 122) {
            result = 12
        }
    } else if (day_type == 'Weekend') {
        if (age <= 18) {
            result = 15
        } else if (age <= 64) {
            result = 20
        } else if (age <= 122) {
            result = 15
        }
    } else if (day_type == 'Holiday') {
        if (age <= 18) {
            result = 5
        } else if (age <= 64) {
            result = 12
        } else if (age <= 122) {
            result = 10
        }
    }

    if (result) {
        console.log(`${result}$`)
    } else {
        console.log("Error!")
    }
}

solve('Holiday', 15)