function editElement(htmlEl, match, replacer) {
    while (htmlEl.textContent.includes(match)) {
        htmlEl.textContent = htmlEl.textContent.replace(match, replacer)
    };
}