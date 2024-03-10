function formatGrade(grade) {
    let adjective = ''
    if (grade < 3) {
        console.log("Fail (2)")
        return
    } else if (grade < 3.5) {
        adjective = 'Poor'
    } else if (grade < 4.5) {
        adjective = 'Good'
    } else if (grade < 5.5) {
        adjective = 'Very good'
    } else if (grade >= 5.5) {
        adjective = 'Excellent'
    }

    console.log(`${adjective} (${grade.toFixed(2)})`);
}

formatGrade(3.33)
formatGrade(4.50)
formatGrade(2.99)