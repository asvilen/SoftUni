class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        if not isinstance(element, str):
            raise ValueError("Element is not a string.")
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        reversed_data = list(reversed(self.data))
        return f"[{', '.join(reversed_data)}]"


