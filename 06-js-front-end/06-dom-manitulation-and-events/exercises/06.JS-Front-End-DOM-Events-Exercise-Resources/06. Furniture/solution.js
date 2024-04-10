function solve() {
  // Textareas
  const textareaElements = document.querySelectorAll("#exercise textarea");
  const inputTAElement = textareaElements.item(0);
  const outputTAElement = textareaElements.item(1);
  // Button elements
  const buttonElements = document.querySelectorAll("#exercise button");
  const generateButton = buttonElements.item(0);
  const buyButton = buttonElements.item(1);
  // Table Body
  const tableBodyElement = document.querySelector("table tbody");
  // Generate listener
  generateButton.addEventListener('click', () => {
    const inputObjArray = JSON.parse(inputTAElement.value);
    for (const obj of inputObjArray) {
      const tableRow = generateRow(obj);
      tableBodyElement.appendChild(tableRow);
    }
  })
  // Buy listener
  buyButton.addEventListener('click', () => {
    let furnitureNames = []
    let totalPrice = 0;
    let totalFactor = 0;
    let counter = 0;
    Array.from(tableBodyElement.children)
      .forEach(furnitureTrElement => {
        const checkmarkElement = furnitureTrElement.querySelector("input[type=checkbox]");
        if (!checkmarkElement.checked) {
          return;
        }
        const paragraphElements = furnitureTrElement.querySelectorAll('td');
        const name = paragraphElements.item(1).textContent;
        const price = Number(paragraphElements.item(2).textContent);
        const dFactor = Number(paragraphElements.item(3).textContent);

        furnitureNames.push(name)
        totalPrice += price
        totalFactor += dFactor
        counter += 1
    const averageDecorationFactor = totalFactor / counter
    outputTAElement.value = [
      `Bought furniture: ${furnitureNames.join(", ")}`,
      `Total price: ${totalPrice.toFixed(2)}`,
      `Average decoration factor: ${averageDecorationFactor}`,
    ].join("\n")
      })
  })

  function generateRow(rowObj) {
    // Row element
    const trow = document.createElement('tr');
    // data- image
    const imgTD = document.createElement('td');
    const imgElement = document.createElement('img');
    imgElement.src = rowObj['img']
    imgTD.appendChild(imgElement)
    // data- checkbox
    const inputTD = document.createElement('td');
    const inputElement = document.createElement('input');
    inputElement.type = "checkbox";
    inputElement.checked = true;
    inputTD.appendChild(inputElement);
    // data- paragraphs
    let paragraphElements = [];
    for (const key in rowObj) {
      if (key !== 'img') {
        const pTD = document.createElement('td');
        const paragraphElement = document.createElement('p');
        paragraphElement.textContent = rowObj[key];
        pTD.appendChild(paragraphElement);
        paragraphElements.push(pTD);
      }
    }
    // Add iamge
    trow.appendChild(imgTD);
    // Add paragraphs
    for (const paragraph of paragraphElements) {
      trow.appendChild(paragraph)
    }
    // Add input
    trow.appendChild(inputTD)

    return trow
  }
}