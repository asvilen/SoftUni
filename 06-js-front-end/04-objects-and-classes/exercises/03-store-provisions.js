function solve(stockList, ordersList) {
    const storeProvisions = {}
    for (i = 0; i < stockList.length; i += 2) {
        let [product, quantity] = [stockList[i], Number(stockList[i+1])]
        storeProvisions[product] = quantity
    }
    for (i = 0; i < ordersList.length; i += 2) {
        let [product, quantity] = [ordersList[i], Number(ordersList[i+1])]
        if (! (product in storeProvisions)) {
            storeProvisions[product] = 0;
        }
        storeProvisions[product] += quantity
    }
    
    for (const product in storeProvisions) {
        console.log(`${product} -> ${storeProvisions[product]}`);
    }
    
}

solve(
    [
    'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
    'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ])