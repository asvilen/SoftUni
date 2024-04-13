function solve(inputArray) {
    const maxBullets = 6
    const n = inputArray.shift();
    let heroes = {};
    for (i = 0; i < n; i++) {
        const [heroName, HP, bullets] = inputArray.shift().split(" ");
        heroes[heroName] = { 
            HP: Number(HP), 
            bullets: Number(bullets) 
        }
    }
    while (inputArray[0] !== "Ride Off Into Sunset") {
        const currentCommandArray = inputArray.shift().split(" - ");
        action = currentCommandArray[0];
        currentName = currentCommandArray[1];
        if (action === "FireShot") {
            const target = currentCommandArray[2];
            const bullets = heroes[currentName].bullets
            if (bullets > 0) {
                const bulletsLeft = bullets - 1
                heroes[currentName]['bullets'] = bulletsLeft
                console.log(`${currentName} has successfully hit ${target} and now has ${bulletsLeft} bullets!`)
            } else {
                console.log(`${currentName} doesn't have enough bullets to shoot at ${target}!`)
            }
        } else if (action === "TakeHit"){
            const damage = Number(currentCommandArray[2]);
            const attacker = currentCommandArray[3];
            const currentHealth = heroes[currentName].HP;
            const leftHealth = currentHealth - damage;
            heroes[currentName].HP = leftHealth;
            if (leftHealth > 0) {
                console.log(`${currentName} took a hit for ${damage} HP from ${attacker} and now has ${leftHealth} HP!`)
            } else {
                delete heroes[currentName]
                console.log(`${currentName} was gunned down by ${attacker}!`)
            }
        } else if (action === "Reload") {
            const currentBulletsCount = heroes[currentName].bullets
            if (currentBulletsCount < 6) {
                heroes[currentName].bullets = 6;
                console.log(`${currentName} reloaded ${6 - currentBulletsCount} bullets!`)
            } else {
                console.log(`${currentName}'s pistol is fully loaded!`)
            }
        } else if (action === "PatchUp") {
            const amount = Number(currentCommandArray[2]);
            const currentHealth = heroes[currentName].HP
            if (currentHealth < 100) {
                heroes[currentName].HP = Math.min((currentHealth + amount), 100);
                console.log(`${currentName} patched up and recovered ${heroes[currentName].HP - currentHealth} HP!`)
            } else {
                console.log(`${currentName} is in full health!`)
            }
        }
    }
    for (const currentName in heroes) {
        const toPirnt = [
            currentName,
            ` HP: ${heroes[currentName].HP}`,
            ` Bullets: ${heroes[currentName].bullets}`,
        ]
        console.log(toPirnt.join("\n"))
    }
}

solve(["2",
"Jesse 100 4",
"Walt 100 5",
"FireShot - Jesse - Bandit",
 "TakeHit - Walt - 30 - Bandit",
 "PatchUp - Walt - 20" ,
 "Reload - Jesse",
 "Ride Off Into Sunset"])