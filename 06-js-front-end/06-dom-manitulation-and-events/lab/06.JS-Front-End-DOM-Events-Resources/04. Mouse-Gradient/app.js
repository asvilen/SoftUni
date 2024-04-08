function attachGradientEvents() {
    const gradientElement = document.getElementById('gradient');
    const resultElement = document.getElementById('result');

    gradientElement.addEventListener('mousemove', (event) => {
        const width = event.target.clientWidth;
        const x = event.offsetX;

        const perc = Math.floor(x / width * 100) + "%";

        resultElement.textContent = perc
    })
}