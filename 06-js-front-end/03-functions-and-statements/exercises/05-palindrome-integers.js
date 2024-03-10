function palindromeIntegers(inputArray) {
    function isPalindrome(number) {
        const numberString = String(number)
        if (numberString === numberString.split("").reverse().join("")) {
            return true
        } else {
            return false
        }
    }
    inputArray.forEach(curNumber => {
        console.log(isPalindrome(curNumber))
    });
}

palindromeIntegers([32,2,232,1010]);