function solve(inputList) {
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }
    
        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }
    for (const cat of inputList) {
        const [name, age] = cat.split(" ")
        const cuurentCat = new Cat(name, age)
        cuurentCat.meow()
    }
}

solve(['Mellow 2', 'Tom 5'])