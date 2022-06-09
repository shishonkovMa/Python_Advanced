class Deque:

    def __init__(self):
        self.deque = []

    def push_front(self, key):
        self.deque.insert(0, key)
        return 'ok'

    def push_back(self, key):
        self.deque.append(key)
        return 'ok'

    def pop_front(self):
        if len(self.deque) == 0:
            return 'error'
        else:
            return self.deque.pop(0)

    def pop_back(self):
        if len(self.deque) == 0:
            return 'error'
        else:
            return self.deque.pop(-1)

    def front(self):
        if len(self.deque) == 0:
            return 'error'
        else:
            return self.deque[0]

    def back(self):
        if len(self.deque) == 0:
            return 'error'
        else:
            return self.deque[-1]

    def clear(self):
        self.deque.clear()
        return 'ok'

    def size(self):
        return len(self.deque)


def process_deque(commands):
    a = Deque()
    total = []
    for i in commands:
        if 'push_front' in i:
            total.append(a.push_front(i.split()[1]))
        elif 'push_back' in i:
            total.append(a.push_back(i.split()[1]))
        elif 'pop_front' in i:
            total.append(a.pop_front())
        elif 'pop_back' in i:
            total.append(a.pop_back())
        elif 'front' in i:
            total.append(a.front())
        elif 'back' in i:
            total.append(a.back())
        elif 'clear' in i:
            total.append(a.clear())
        elif 'size' in i:
            total.append(a.size())

    return total


if __name__ == "__main__":
    test_cmd = ["push_front 1", "push_front 2", "push_back 6", "front", "back", "clear", "size", "back"]
    # should print ["ok", "ok", "ok", 2, 6, "ok", 0, "error"]
    print(process_deque(test_cmd))

    test_cmd = ["pop_front", "back", "push_back 2", "size"]
    # should print ["error", "error", "ok", 1]
    print(process_deque(test_cmd))

    test_cmd = ["push_back 1", "push_front 10", "push_front 4", "push_front 5", "back", "pop_back", "pop_back", "back"]
    # should print ["ok", "ok", "ok", "ok", 1, 1, 10, 4]
    print(process_deque(test_cmd))

