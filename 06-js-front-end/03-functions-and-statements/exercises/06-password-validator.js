function passwordValidator(password) {
    let result = [];
    let valid = true;
    // const numCount = password.match(/[0-9]/g).length
    if (password.length < 6 || password.length > 10) {
        valid = false
        result.push("Password must be between 6 and 10 characters")
    }
    if(! password.match(/^[a-zA-Z0-9]*$/)){
        valid = false
        result.push("Password must consist only of letters and digits")
    } 
    if(password.match(/[0-9]/g) === null || password.match(/[0-9]/g).length < 2) {
        valid = false
        result.push("Password must have at least 2 digits")
    } 
    if (valid) {
        result.push("Password is valid")
    }
    console.log(result.join("\n"));
}

passwordValidator('logIn');

// console.log(('asda'.match(/[0-9]/g) !== null))