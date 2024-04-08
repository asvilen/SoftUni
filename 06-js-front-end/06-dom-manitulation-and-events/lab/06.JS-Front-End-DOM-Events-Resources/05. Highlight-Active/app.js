function focused() {
    const divElement = document.querySelector("body div");
    const divsList = Array
        .from(divElement.children)

    for (const div of divsList) {
        
        const inputEl = div.querySelector("input");
        // Add focus class when focused
        inputEl.addEventListener('focus', () => {
            div.classList.add('focused')
        })
        // Remove focus class when blurred
        inputEl.addEventListener('blur', () => {
            div.classList.remove('focused')
        })
    }
    }