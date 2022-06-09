class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def __init__(self):
        super().__init__()
        self.lst = []

    def append(self, number):
        if number <= 0:
            raise NonPositiveError
        else:
            super().append(number)
        return self.lst

# Авторское решение

# class PositiveList(list):
#     def append(self, x):
#         if x > 0:
#             super().append(x)
#         else:
#             raise NonPositiveError
