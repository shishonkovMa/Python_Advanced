class Flash:
    def __init__(self, capacity):
        self.capacity = capacity

    def write(self, filesize):
        if self.capacity >= filesize:
            self.capacity -= filesize
        else:
            raise ValueError
