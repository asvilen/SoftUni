function solve(commandsList) {
    const moviesList = []
    for (const command of commandsList) {
        if (command.includes('addMovie')) {
            const movieName = command.split('addMovie ')[1]
            moviesList.push({name: movieName})
        } else if (command.includes('directedBy')) {
            const [movieName, directorName] = command.split(' directedBy ')
            for (const movie of moviesList) {
                if (movie.name === movieName) {
                    movie['director'] = directorName
                }
            }
        } else if (command.includes(' onDate ')) {
            const [movieName, date] = command.split(' onDate ')
            for (const movie of moviesList) {
                if (movie.name === movieName) {
                    movie['date'] = date
                }
            }
        }
    }
    const validMovies = moviesList.filter(movie => {
        return movie.name && movie.date && movie.director
    })
    validMovies.forEach(movie => console.log(JSON.stringify(movie)))
}

solve([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
    ])
console.log()
solve([
    'addMovie The Avengers',
    'addMovie Superman',
    'The Avengers directedBy Anthony Russo',
    'The Avengers onDate 30.07.2010',
    'Captain America onDate 30.07.2010',
    'Captain America directedBy Joe Russo'
    ])