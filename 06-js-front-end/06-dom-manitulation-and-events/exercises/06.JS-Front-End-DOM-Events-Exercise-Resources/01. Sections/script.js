function create(words) {

   function createDiv(word) {
      const div = document.createElement('div');
      const paragraph = document.createElement('p');
      paragraph.textContent = word
      paragraph.style.display = 'none'
      div.appendChild(paragraph)
      return div
   }

   const content = document.getElementById('content')
   for (const word of words) {
      content.appendChild(createDiv(word))
   }

   const divElement =  document.querySelectorAll('#content div')
   const divArray = Array.from(divElement)
   for (const el of divArray) {
      console.log(el)
      el.addEventListener('click', () => {
         const pElement = el.querySelector("p");
         pElement.style.display = 'inline'
      })
   }
}