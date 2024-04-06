function create(words) {

   function createDiv(word) {
      const div = document.createElement('div');
      const paragraph = document.createElement('p');
      paragraph.append(word)
      paragraph.style.display = 'none'
      div.appendChild(paragraph)
      return div
   }

   const divElement = document.getElementById('content')
   for (const word of words) {
      divElement.appendChild(createDiv(word))
   }

   const pElement =  document.querySelectorAll('#content div p')
   console.log(pElement);
   pElement.forEach(function(item) {
      item.addEventListener("click", function () {
         // item.style.display = 'block';
         console.log('You clicked the div');
      })
   })

   return divElement
}