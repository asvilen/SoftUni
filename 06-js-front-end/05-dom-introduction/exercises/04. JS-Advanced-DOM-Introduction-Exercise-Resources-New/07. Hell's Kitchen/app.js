function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      const textAreaEl = document.getElementsByTagName("textarea")
      const text = textAreaEl.item(0).value
      const inputArray = text
         .split('"')
         .filter(el => !['[', ']', ','].includes(el))
      let highestAvgSalary = 0
      let highestSalary = 0
      let highestAvgSalaryTeam = ''
      let higherSalaryWorkersInfo = {}
      for (const restInfo of inputArray) {
         const [name, averageSalary, bestSalary, workersInfoObj] = getRestaurantStats(restInfo)
         if (highestAvgSalary < averageSalary) {
            [highestAvgSalaryTeam, highestAvgSalary, highestSalary, higherSalaryWorkersInfo] = [name, averageSalary, bestSalary, workersInfoObj];
         }
      }
      // Best Restaurant
      const bestRestaurantOutputEl = document.querySelectorAll("#bestRestaurant p").item(0);
      bestRestaurantOutputEl.textContent = `Name: ${highestAvgSalaryTeam} Average Salary: ${highestAvgSalary.toFixed(2)} Best Salary: ${highestSalary.toFixed(2)}`;
      // Best Workers
      const workersOutputEl = document.querySelectorAll("#workers p").item(0);
      let workersString = ''
      for (const key in higherSalaryWorkersInfo) {
         workersString += `Name: ${key} With Salary: ${higherSalaryWorkersInfo[key]} `
      }
      workersOutputEl.textContent = workersString

      function getRestaurantStats(restArray) {
         const restArraySplitted = restArray.split(" - ");
         const name = restArraySplitted[0];
         const workers = restArraySplitted[1].split(", ");
         let totalSalaries = 0;
         let bestSalary = 0
         let workersInfoObj = {}
         for (const workerInfo of workers) {
            const workersInfoArray = workerInfo.split(" ")
            const currentWorker = workersInfoArray[0]
            const currentSalary = Number(workersInfoArray[1]);
            workersInfoObj[currentWorker] = currentSalary
            totalSalaries += currentSalary;
            if (currentSalary > bestSalary) {
               bestSalary = currentSalary
            }
         }
         const averageSalary = (totalSalaries / workers.length)
         return [name, averageSalary, bestSalary, workersInfoObj]
      }
   }
}