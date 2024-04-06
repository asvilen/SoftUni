function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const tbodyEl = document.querySelectorAll('.container tbody tr')
      const searchTerm = document.getElementById('searchField');
      console.log(searchTerm.value)
      // let nodes = tbodyEl
      // console.log(nodes);
      for (i = 0; i < tbodyEl.length; i ++) {
         tbodyEl[i].classList.remove('select')
         if (tbodyEl[i].textContent.includes(searchTerm.value)) {
            console.log(tbodyEl[i].textContent);
            tbodyEl[i].classList.add('select')
      }
      }

   }
}