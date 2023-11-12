class User:
    def __init__(self, user_id: int, username: str) -> object:
        self.username = username
        self.user_id = user_id
        self.books = []

    def info(self):
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"