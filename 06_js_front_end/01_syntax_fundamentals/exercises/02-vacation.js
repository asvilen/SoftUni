function solve(ppl, type, day) {
    let price;
    if (day === 'Friday') {
        if (type == 'Students') {
            price = 8.45
        } else if (type === 'Business') {
            price = 10.9
        } else if (type === 'Regular') {
            price = 15
        }
    } else if (day === 'Saturday') {
        if (type == 'Students') {
            price = 9.8
        } else if (type === 'Business') {
            price = 15.6
        } else if (type === 'Regular') {
            price = 20
        }
    } else if (day === 'Sunday') {
        if (type == 'Students') {
            price = 10.46
        } else if (type === 'Business') {
            price = 16
        } else if (type === 'Regular') {
            price = 22.5
        }
    }

    if (type === 'Students' && ppl >= 30) {
        price = price * 0.85
    }
    if (type === 'Business' && ppl >= 100) {
        ppl = ppl - 10
    }
    if (type === 'Regular' && ppl >= 10 && ppl <= 20) {
        price = price * 0.95
    }


    return `Total price: ${(ppl * price).toFixed(2)}`
}

console.log(solve(
    40,
    "Regular",
    "Saturday"    
));