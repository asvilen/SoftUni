const baseURL = "http://localhost:3030/jsonstore/gifts";

// HTML elements
const loadButton = document.getElementById('load-presents');
const giftListElement = document.getElementById('gift-list');
const addGiftElement = document.getElementById('add-present');
const editGiftElement = document.getElementById('edit-present');
const inputGiftElement = document.getElementById('gift');
const inputNameElement = document.getElementById('for')
const inputPriceElement = document.getElementById('price');

let currentGiftId = '';

loadButton.addEventListener('click', loadData)

addGiftElement.addEventListener('click', async () => {
    const postReData = getInputData()
    const response = await fetch(baseURL, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(postReData)
    })

    validateResponse(response);
    clearInput();
    loadData();
})

async function loadData() {
    console.log("Pulling data")
    // Fetch data
    const response = await fetch(baseURL);
    const data = await response.json();
    const giftsArray = Object.values(data);
    console.log(giftsArray)
    // Prepare list element
    const giftListElement = document.getElementById('gift-list');
    giftListElement.textContent = '';
    // Loop through data adding each sock to the giftList
    for (const sock of giftsArray) {
        const present = sock.gift;
        const name = sock.for;
        const price = sock.price;
        // Add tasks to gift-list
        // Buttons
        const changeButtonElement = document.createElement('button');
        const deleteButtonElement = document.createElement('button');
        const buttonsContainerElement = document.createElement('div');
        changeButtonElement.classList.add('change-btn');
        deleteButtonElement.classList.add('delete-btn');
        buttonsContainerElement.classList.add('buttons-container');
        changeButtonElement.textContent = "Change";
        deleteButtonElement.textContent = "Delete";
        buttonsContainerElement.appendChild(changeButtonElement);
        buttonsContainerElement.appendChild(deleteButtonElement);
        // Content
        const presentElement = document.createElement('p');
        const nameElement = document.createElement('p');
        const priceElement = document.createElement('p');
        const contentDivContainerElement = document.createElement('div');
        presentElement.textContent = present;
        nameElement.textContent = name;
        priceElement.textContent = price;
        contentDivContainerElement.appendChild(presentElement);
        contentDivContainerElement.appendChild(nameElement);
        contentDivContainerElement.appendChild(priceElement);
        // Create Sock
        const giftSockElement = document.createElement('divz');
        giftSockElement.classList.add('gift-sock');
        // Append elements
        giftSockElement.appendChild(contentDivContainerElement);
        giftSockElement.appendChild(buttonsContainerElement);
        giftListElement.appendChild(giftSockElement);
        console.log("Data loaded successfully!");


        // Change button logic
        changeButtonElement.addEventListener('click', () => {
            currentGiftId = sock._id
            // Populate inputs
            inputGiftElement.value = present;
            inputNameElement.value = name;
            inputPriceElement.value = price;
            // Remove gift from tree
            giftSockElement.remove()
            // Activate EDIT, Deactivate ADD
            activateEditButtons();
            // Edit Button Logic
            editGiftElement.addEventListener('click', async () => {
                // Get input data
                const putData = getInputData()
                const putURL = `${baseURL}/${currentGiftId}`
                const response = await fetch(putURL, {
                    method: "PUT",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({...putData, _id: currentGiftId}),
                })
                validateResponse(response);
                clearInput();
                loadData();
                activateAddButtons();
            })
        })
    }
}

function validateResponse(response) {
    if (!response.ok) {
        console.log("Something went wrong!");
    } else {
        console.log("Post request was successful!");
    }
}

function clearInput() {
    inputGiftElement.value = '';
    inputNameElement.value = '';
    inputPriceElement.value = '';
}

function activateEditButtons() {
    editGiftElement.removeAttribute('disabled');
    addGiftElement.setAttribute('disabled', 'disabled');
}
function activateAddButtons() {
    addGiftElement.removeAttribute('disabled');
    editGiftElement.setAttribute('disabled', 'disabled');
}

function getInputData() {
    return {
        gift: inputGiftElement.value,
        for: inputNameElement.value,
        price: inputPriceElement.value,
    }
}