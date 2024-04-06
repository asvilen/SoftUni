function solve() {
  // Refresh
  const outputDiv = document.getElementById("output");
  outputDiv.textContent = "";
  // Get needed elements
  const textAreaEl = document.getElementById('input');
  const divOutputEl = document.getElementById('output');

  let result = textAreaEl.value
    .split(".")
    .filter(el => !!el)
    .reduce((result, sentence, i) => {
      const resultIndex = Math.floor(i / 3)
      if (!result[resultIndex]) {
        result[resultIndex] = []
      }
      result[resultIndex].push(sentence.trim())
      return result;
    }, [])
    .map(sentences => `<p>${sentences.join(". ")}.</p>`)
    .join("\n")

    divOutputEl.innerHTML = result
  
}