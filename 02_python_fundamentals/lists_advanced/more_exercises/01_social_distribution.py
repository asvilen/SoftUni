the_input = input().split(", ")
population = [int(number) for number in the_input]
minimum_wealth = int(input())
max_wealth_per_person = sum(population) / len(population)
if max_wealth_per_person < minimum_wealth:
    print("No equal distribution possible")
else:
    for index, person in enumerate(population):
        wealthiest_person_index = population.index(max(population))
        if person < minimum_wealth:
            needed_wealth = minimum_wealth - person
            person = minimum_wealth
            population[wealthiest_person_index] = max(population) - needed_wealth
            population[index] = minimum_wealth
    print(population)