function solve(inputList) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }
    function printSongs(songList) {
        for (const song of songList) {
            console.log(song.name)
        }
    }
    const elements = inputList[0];
    const elList = inputList.slice(1, inputList.length - 1);
    const command = inputList[inputList.length - 1]
    const album = [];
    for (const song of elList) {
        const [typeList, name, time] = song.split("_")
        const currentSong = new Song(typeList, name, time)
        album.push(currentSong)
    }
    if (command == 'all') {
        printSongs(album)
    } else {
        printSongs(album.filter(song => song.typeList === command))
    }
}

solve([4,
    'favourite_DownTown_3:14',
    'listenLater_Andalouse_3:24',
    'favourite_In To The Night_3:58',
    'favourite_Live It Up_3:48',
    'listenLater'])