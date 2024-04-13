window.addEventListener("load", solve);

function solve() {
  // HTML Elements
    const addButtonElemnent = document.getElementById('add-btn');
    const inputNameElement = document.getElementById('name');
    const inputPhoneElement = document.getElementById('phone');
    const inputSelectElement = document.getElementById('category');
    const checkListElement = document.getElementById('check-list');
    const contactListElement = document.getElementById('contact-list');

    addButtonElemnent.addEventListener('click', () => {
      const inputData = getInputs();
      const listItemElement = document.createElement('li');
      // Buttons
      const buttonsDivElement = document.createElement('div');
      const editButtonElement = document.createElement('button');
      const saveButtonElement = document.createElement('button');
      editButtonElement.classList.add('edit-btn');
      saveButtonElement.classList.add('save-btn');
      buttonsDivElement.appendChild(editButtonElement);
      buttonsDivElement.appendChild(saveButtonElement);
      // Article
      const articleContainerElement = document.createElement('article');
      const namePElement = document.createElement('p');
      const phonePElement = document.createElement('p');
      const categoryPElement = document.createElement('p');
      namePElement.textContent = `name:${inputData.name}`;
      phonePElement.textContent = `phone:${inputData.phone}`;
      categoryPElement.textContent = `category:${inputData.category}`;
      articleContainerElement.appendChild(namePElement);
      articleContainerElement.appendChild(phonePElement);
      articleContainerElement.appendChild(categoryPElement);
      // Append to List Item
      listItemElement.appendChild(articleContainerElement);
      listItemElement.appendChild(buttonsDivElement);
      // Append to Unordered List
      checkListElement.appendChild(listItemElement);
      // Clear inputs
      clearInputs();

      editButtonElement.addEventListener('click', () => {
        // Get values by id
        console.log("Editing contact")
        const articleElement = document.querySelector("ul article");
        const paragraphs = articleElement.children;
        console.log(paragraphs);
        console.log(paragraphs[0]);
        console.log(paragraphs[0].textContent);

        const name = paragraphs[0].textContent.split(":")[1];
        const phone = paragraphs[1].textContent.split(":")[1];
        const category = paragraphs[2].textContent.split(":")[1];
        
        // Populate Input fields
        inputNameElement.value = name;
        inputPhoneElement.value = phone;
        inputSelectElement.value = category;
        // Remove List Item
        listItemElement.remove()
      })

      saveButtonElement.addEventListener('click', () => {
        // Append to contact-list
        // 1. Get values
        const articleElement = document.querySelector("ul article");
        const paragraphs = articleElement.children;
        const name = paragraphs[0].textContent.split(":")[1];
        const phone = paragraphs[1].textContent.split(":")[1];
        const category = paragraphs[2].textContent.split(":")[1];
        const saveListItemElement = document.createElement('li');
        // 2. Create Button
        const deleteButtonElement = document.createElement('button');
        deleteButtonElement.classList.add('del-btn');
        // 3.Create Article
        const articleContainerElement = document.createElement('article');
        const namePElement = document.createElement('p');
        const phonePElement = document.createElement('p');
        const categoryPElement = document.createElement('p');
        namePElement.textContent = `name:${name}`;
        phonePElement.textContent = `phone:${phone}`;
        categoryPElement.textContent = `category:${category}`;
        articleContainerElement.appendChild(namePElement);
        articleContainerElement.appendChild(phonePElement);
        articleContainerElement.appendChild(categoryPElement);
        // 4. Append to List Item
        saveListItemElement.appendChild(articleContainerElement);
        saveListItemElement.appendChild(deleteButtonElement);
        // 5. Append to Unordered List
        contactListElement.appendChild(saveListItemElement);
        // Remove from check-list
        listItemElement.remove()


        deleteButtonElement.addEventListener('click', () => {
          // Delete the element 
          saveListItemElement.remove();
        })
      })
    })

    function getInputs() {
      return {
        name: inputNameElement.value,
        phone: inputPhoneElement.value,
        category: inputSelectElement.value,
      }
    }

    function clearInputs() {
      inputNameElement.value = '';
      inputPhoneElement.value = '';
      inputSelectElement.value = '';
    }
  }
  