class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.counter == self.number:
            raise StopIteration

        if self.number > len(self.sequence):
            self.sequence += self.sequence

        value = self.sequence[self.counter]
        self.counter += 1
        return value
