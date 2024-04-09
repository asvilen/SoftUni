function lockedProfile() {
    const profileElements = document.querySelectorAll(".profile")

    const profileArray = Array.from(profileElements)
    for (const profile of profileArray) {
            const button = profile.querySelector("button");
            button.addEventListener('click', () => {
                const status = profile.querySelector("input[type = radio]:checked").value;
                const hiddenDiv = profile.querySelector("div");
                // MASK
                if (!hiddenDiv.id.includes("!")) {
                    if (status === 'unlock') {
                        // Mask info - add "!"
                        hiddenDiv.id = "!" + hiddenDiv.id
                        // Update button text
                        button.textContent = 'Hide it'
                        return;
                    }
                }
                // UNMASK
                if (hiddenDiv.id.includes("!")) {
                    if (status === 'unlock') {
                        // Unmask info - remove added "!"
                        const originalID = hiddenDiv.id.slice(1)
                        hiddenDiv.id = originalID
                        // Update button text
                        button.textContent = 'Show more'
                        return;
                    }
                }
            })
    }
}