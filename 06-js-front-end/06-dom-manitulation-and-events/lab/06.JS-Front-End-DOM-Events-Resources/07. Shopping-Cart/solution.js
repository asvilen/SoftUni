function solve() {
   const checkoutButtonElement = document.querySelector('.checkout');
   const productsElement = document.querySelectorAll(".product");
   const textareaElement = document.querySelector('textarea');
   const productsArray = Array.from(productsElement);

   let boughtProducts = {};
   for (const productElement of productsArray) {
      const addButtonElement = productElement.querySelector('.add-product');
      const productName = productElement.getElementsByClassName('product-title').item(0).textContent;
      const productPrice = Number(productElement.getElementsByClassName('product-line-price').item(0).textContent);

      addButtonElement.addEventListener('click', () => {
         // Add only if it does not exist already
         if (!boughtProducts[productName]) {
            // Add to object
            boughtProducts[productName] = productPrice
            // Add products to textarea
            result = `Added ${productName} for ${productPrice.toFixed(2)} to the cart.\n`
            textareaElement.textContent += result
         }
      })
   }

   checkoutButtonElement.addEventListener('click', () => {
      // Calculate total & create products list
      let list = [];
      let sum = 0;
      for (const product in boughtProducts) {
         list.push(product)
         sum += boughtProducts[product]
      }
      // Add result to text area
      result = `You bought ${list.join(", ")} for ${sum.toFixed(2)}.`
      textareaElement.textContent += result
      // disable buttons (add, checkout)
      for (const productElement of productsArray) {
         const addButtonElement = productElement.querySelector('.add-product');
         addButtonElement.disabled = true
         checkoutButtonElement.disabled = true
      }
   })

}