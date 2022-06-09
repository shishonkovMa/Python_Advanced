class FlashError(Exception):
    pass


class FlashMaxFileSizeError(FlashError):
    pass


class FlashMemoryLimitError(FlashError):
    pass


class Flash:
    def __init__(self, capacity, max_file_size=None):
        self.capacity = capacity
        self.max_file_size = max_file_size

    def write(self, v):
        if self.max_file_size is None or v <= self.max_file_size:
            if self.capacity >= v:
                self.capacity -= v
            else:
                raise FlashMemoryLimitError() from FlashError
        else:
            raise FlashMaxFileSizeError() from FlashError
