class Trainer:
    id = 1

    def __init__(self, name: str):
        self.id = self.get_next_id()
        self.name = name

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        current_id = Trainer.id
        Trainer.id += 1
        return current_id
