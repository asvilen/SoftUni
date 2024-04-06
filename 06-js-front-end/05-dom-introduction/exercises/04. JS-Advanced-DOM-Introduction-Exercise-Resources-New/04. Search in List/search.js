function search() {
   const searchTerm = document.getElementById('searchText').value
   const townsEl = document.querySelectorAll('#towns li')
   const resultEl = document.getElementById('result')
   let numMatches = 0
   for (let town of townsEl) {
      town.style.fontWeight = 'normal';
      town.style.textDecoration = 'none'
      townName = town.textContent
      if (searchTerm && townName.includes(searchTerm)) {
         town.style.textDecoration = 'underline';
         town.style.fontWeight = 'undebolderrline';
         numMatches += 1
      }
   }
   resultEl.textContent = `${numMatches} matches found`;
}
