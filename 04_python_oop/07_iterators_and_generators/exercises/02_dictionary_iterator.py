class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dict_tuple = tuple(dictionary.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dict_tuple):
            raise StopIteration
        value = self.dict_tuple[self.index]
        self.index += 1
        return value
