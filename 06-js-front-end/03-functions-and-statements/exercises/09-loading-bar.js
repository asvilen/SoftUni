function loadingBar(load) {
    if (load !== 100) {
        const loader = load / 10
        const perc = "%".repeat(loader)
        const dots = ".".repeat(10 - loader)
        return `${load}% [${perc}${dots}]\nStill loading...`
    } else {
        return "100% Complete!\n[%%%%%%%%%%]"
    }
}

console.log(loadingBar(100));