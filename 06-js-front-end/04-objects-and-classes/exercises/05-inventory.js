function solve(inputString) {
    const heroesList = []
    for (const hero of inputString) {
        const [name, level, items] = hero.split(" / ")
        heroesList.push({
            name,
            level: Number(level),
            items,
        })
    }
    heroesList.sort((a, b) => a.level - b.level)
    for (const hero of heroesList) {
        console.log(`Hero: ${hero.name}\nlevel => ${hero.level}\nitems => ${hero.items}`);
    }
}

solve([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ])

solve([
    'Batman / 2 / Banana, Gun',
    'Superman / 18 / Sword',
    'Poppy / 28 / Sentinel, Antara'
    ])