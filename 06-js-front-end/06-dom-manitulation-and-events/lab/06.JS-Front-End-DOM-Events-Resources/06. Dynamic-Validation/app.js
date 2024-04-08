function validate() {
    const emailInputElement = document.getElementById('email')

    emailInputElement.addEventListener('change', () => {
        const emailAddress = emailInputElement.value;
        const pattern = /^[a-z]*@[a-z]*\.[a-z]*/g
        const matches = emailAddress.match(pattern)
        if (!matches) {
            emailInputElement.classList.add('error')
        }
        if (matches) {
            emailInputElement.classList.remove('error')
        }
    })
}