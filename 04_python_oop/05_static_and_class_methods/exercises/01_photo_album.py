class PhotoAlbum:
    _photos_per_page = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for page in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        num_pages = photos_count // cls._photos_per_page
        num_pages += 0 if photos_count % cls._photos_per_page == 0 else 1
        return cls(num_pages)

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return (f"{label} photo added successfully "
                        f"on page {page + 1} slot {len(self.photos[page])}")
        return "No more free slots"

    def display(self):
        info = "-" * 11 + "\n"
        for page in self.photos:
            info += " ".join([f"[]" for photo in page])
            info += "\n" + "-" * 11 + "\n"
        return info


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
