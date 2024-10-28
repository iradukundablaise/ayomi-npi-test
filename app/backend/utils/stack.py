class Stack():
    def __init__(self):
        self.items = []

    def top(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        last = self.items[-1]
        self.items = self.items[:-1]
        return last
    
    def is_empty(self):
        return len(self.items) == 0

