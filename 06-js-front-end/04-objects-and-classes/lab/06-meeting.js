function solve(inputString) {
    let calendar = {}
    for (const pMeeting of inputString) {
        const [day, name] = pMeeting.split(" ")
        if (day in calendar) {
            console.log(`Conflict on ${day}!`);
        } else {
            calendar[day] = name
            console.log(`Scheduled for ${day}`)
        }
    }
    for (const day in calendar) {
        console.log(`${day} -> ${calendar[day]}`)
    }
}

solve(['Monday Peter',
'Wednesday Bill',
'Monday Tim',
'Friday Tim'])