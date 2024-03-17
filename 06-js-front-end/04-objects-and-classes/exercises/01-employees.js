function solve(employeesList) {
    let employeesObj = {}
    for (const name of employeesList) {
        employeesObj[name] = name.length
    }
    for (const name in employeesObj) {
        console.log(`Name: ${name} -- Personal Number: ${employeesObj[name]}`);
    }
}

solve([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
])