class Stack:
    def __init__(self):
        self.stack = []

    def __bool__(self):
        return bool(self.stack)

    def push(self, elem):
        if self.stack:
            self.stack.append((elem, min(elem, self.stack[-1][1])))
        else:
            self.stack.append((elem, elem))

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()[0]
        else:
            raise IndexError('pop from an empty queue')


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, elem):
        self.s1.push(elem)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.push(self.s1.pop())
        return self.s2.pop()
