class Stack:

    def __init__(self, items=None, limit=100):
        if items is None:
            self.items = []
        else:
            self.items = list(items)   
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        """
        Returns how far the element is from the top of the stack.
        Top element = 0
        Returns -1 if target not found.
        """
        if target in self.items:
            return (len(self.items) - 1) - self.items.index(target)
        return -1

