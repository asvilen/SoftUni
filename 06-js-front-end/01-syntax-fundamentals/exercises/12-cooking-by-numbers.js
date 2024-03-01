function solve(number, par1, par2, par3, par4, par5) {
    const calculator = {
        'chop'  : (num) => num / 2,
        'dice'  : (num) => Math.sqrt(num),
        'spice' : (num) => num + 1,
        'bake'  : (num) => num * 3,
        'fillet': (num) => num * 0.8,
    }
    let result = number;
    for (const command of [par1, par2, par3, par4, par5]) {
        result = calculator[command](result)
        console.log(result);
    }
}

solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet')
