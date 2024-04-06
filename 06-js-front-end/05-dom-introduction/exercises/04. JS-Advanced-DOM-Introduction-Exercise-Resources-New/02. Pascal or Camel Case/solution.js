function solve() {
  const input = document.getElementById('text').value;
  const convention = document.getElementById('naming-convention').value;
  const wordsList = input.toLowerCase().split(" ")
  const resultElement = document.getElementById('result')
  let result = ""
  if (convention === "Pascal Case") {
    result = toPascal(wordsList)
  } else if (convention == "Camel Case") {
    result = toCamel(wordsList)
  } else {
    result = 'Error!'
  }
  resultElement.textContent = result

  function toPascal(wordsArray) {
    let result = ""
    for (const word of wordsArray) {
      result += word.charAt(0).toUpperCase() + word.slice(1)
    }
    return result
  }

  function toCamel(wordsArray) {
    let result = ""
    for (let i = 0; i < wordsArray.length; i++) {
      if (i === 0) {
        result += wordsArray[i]
      } else {
        result += wordsArray[i].charAt(0).toUpperCase() + wordsArray[i].slice(1)
      }
    }
    return result
  }
}