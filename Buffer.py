class Buffer:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.container = []

    def add(self, *a):
        x = list(i for i in a)
        dlina = len(x) + len(self.container)
        if dlina < self.maxsize:
            self.container.extend(x)
        elif dlina > self.maxsize:
            dlina1 = dlina
            x1 = x
            while dlina1 >= self.maxsize:
                self.container.extend(x1)
                x1 = []
                print(sum(self.container[:self.maxsize]))
                dlina1 = len(self.container[self.maxsize:])
                self.container = self.container[self.maxsize:]
            self.container = []
            if -dlina + dlina // self.maxsize * self.maxsize == 0:
                pass
            else:
                self.container.extend(x[-dlina + dlina // self.maxsize *
                                        self.maxsize:])
        elif dlina == self.maxsize:
            self.container.extend(x)
            print(sum(self.container[:self.maxsize]))
            self.container = []
        return self.container

    def get_current_part(self):
        return self.container
