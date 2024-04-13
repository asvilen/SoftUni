const baseUrl = "http://localhost:3030/jsonstore/games";

// HTML elements
const loadPresentsButton = document.getElementById('load-games');
const addPresentButton = document.getElementById('add-game');
const editPresentButton = document.getElementById('edit-game');
const giftListElement = document.getElementById('games-list');
const giftInputElement = document.getElementById('g-name');
const forInputElement = document.getElementById('type');
const priceInputElement = document.getElementById('players');
const formContainerElement = document.getElementById('form');

loadPresentsButton.addEventListener('click', loadPresents);

addPresentButton.addEventListener('click', addPresent);

editPresentButton.addEventListener('click', editGift);

giftListElement.addEventListener('click', deleteGift);

function addPresent() {
    // Get input data
    const present = getInputData();

    // Post request
    fetch(baseUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(present)
    })
        .then(res => {
            if (!res.ok) {
                return;
            }

            // clear input fields
            clearInputFields();

            // fetch presents
            return loadPresents();
        });
}

async function loadPresents() {
    const response = await fetch(baseUrl);
    const presentsResult = await response.json();

    giftListElement.innerHTML = '';

    const giftListFragment = document.createDocumentFragment();

    Object
        .values(presentsResult)
        .forEach(present => {
            giftListFragment.appendChild(createGiftSockElement(present));
        })

    giftListElement.appendChild(giftListFragment);
}

function createGiftSockElement(present) {
    const changeButtonElement = document.createElement('button');
    changeButtonElement.classList.add('change-btn');
    changeButtonElement.textContent = 'Change';
    changeButtonElement.addEventListener('click', (e) => changeGift(e, present));

    const deleteButtonElement = document.createElement('button');
    deleteButtonElement.classList.add('delete-btn');
    deleteButtonElement.textContent = 'Delete';

    const buttonsDivElement = document.createElement('div');
    buttonsDivElement.classList.add('buttons-container');
    buttonsDivElement.appendChild(changeButtonElement);
    buttonsDivElement.appendChild(deleteButtonElement);

    const giftPElement = document.createElement('p');
    giftPElement.textContent = present.name;

    const forPElement = document.createElement('p');
    forPElement.textContent = present.type;

    const pricePElement = document.createElement('p');
    pricePElement.textContent = present.players;

    const contentDivElement = document.createElement('div');
    contentDivElement.classList.add('content');
    contentDivElement.appendChild(giftPElement);
    contentDivElement.appendChild(forPElement);
    contentDivElement.appendChild(pricePElement);

    const giftSockDivElement = document.createElement('div');
    giftSockDivElement.classList.add('board-game');
    giftSockDivElement.appendChild(contentDivElement);
    giftSockDivElement.appendChild(buttonsDivElement);

    giftSockDivElement.setAttribute('data-id', present._id);

    return giftSockDivElement;
}

function changeGift(e, present) {
    //  removepresent from list
    // const giftElement = e.currentTarget.closest('.gift-sock');
    const giftElement = e.currentTarget.parentElement.parentElement; // Don't do this unless judge :)
    giftElement.remove();

    //  populate input fields
    giftInputElement.value = present.name;
    forInputElement.value = present.type;
    priceInputElement.value = present.players;

    //  add id as attribute
    formContainerElement.setAttribute('data-id', present._id);

    // activate edit button
    editPresentButton.removeAttribute('disabled');

    // decativate create button
    addPresentButton.setAttribute('disabled', 'disabled');
}

function editGift() {
    // Get data from inputs
    const present = getInputData();

    // get giftid
    const giftId = formContainerElement.getAttribute('data-id');

    // remove data-id attribute
    formContainerElement.removeAttribute('data-id');

    // send put request
    fetch(`${baseUrl}/${giftId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ _id: giftId, ...present }),
        // body: JSON.stringify(Object.assign({}, present, { _id: giftId })),
    })
        .then(res => {
            if (!res.ok) {
                return;
            }

        // fetch presents
        loadPresents();

        // deactivate edit button
        editPresentButton.setAttribute('disabled', 'disabled');

        // activate add button
        addPresentButton.removeAttribute('disabled');

        // clear inputs
        clearInputFields();
        });
}

// This is event delegation
function deleteGift(e) {
    if (e.target.tagName !== 'BUTTON' || !e.target.classList.contains('delete-btn'))  {
        return;
    }

    // Get gift  element
    const giftElement = e.target.parentElement.parentElement;

    // Get id
    const giftId = giftElement.getAttribute('data-id');

    // Delete request
    fetch(`${baseUrl}/${giftId}`, {
        method: 'DELETE',
    })
        .then(res => {
            if (!res.ok) {
                return;
            }
            
            // remove from giftlist
            giftElement.remove();
        });
}

function clearInputFields() {
    giftInputElement.value = '';
    forInputElement.value = '';
    priceInputElement.value = '';
}

function getInputData() {
    return {
        name: giftInputElement.value,
        type: forInputElement.value,
        players: priceInputElement.value
    }
};