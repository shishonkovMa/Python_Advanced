import operator
import copy


class MatrixSizeError(Exception):
    pass


class Matrix:
    def __init__(self, lst):
        self.lst = copy.deepcopy(lst)

    def __str__(self):
        lst_of_strs = ['\t'.join(map(str, row)) for row in self.lst]
        return '\n'.join(lst_of_strs)

    def size(self):
        return len(self.lst), len(self.lst[0])

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if other.lst == self.lst:
                return True
            else:
                return False
        else:
            raise TypeError()

    def __add__(self, operand_2):
        if isinstance(operand_2, Matrix):
            if self.size() == operand_2.size():
                a = [[operator.add(a, b) for a, b in zip(row_1, row_2)]
                     for row_1, row_2 in zip(self.lst, operand_2.lst)]
                return Matrix(a)
            else:
                raise MatrixSizeError()
        else:
            raise TypeError()

    def __sub__(self, operand_2):
        if isinstance(operand_2, Matrix):
            if self.size() == operand_2.size():
                a = [[operator.sub(a, b) for a, b in zip(row_1, row_2)]
                     for row_1, row_2 in zip(self.lst, operand_2.lst)]
                return Matrix(a)
            else:
                raise MatrixSizeError()
        else:
            raise TypeError()

    def __mul__(self, operand_2):
        def mul(row, col):
            return sum(a * b for a, b in zip(row, col))

        if isinstance(operand_2, Matrix):
            m, o = self.size(), operand_2.size()
            if m[1] == o[0]:
                res_mtrx = Matrix([])
                for row in self.lst:
                    if isinstance(operand_2, int):
                        res_mtrx.lst.append([col * operand_2 for col in row])
                    elif not isinstance(operand_2, int):
                        res_mtrx.lst.append([mul(row, col)
                                            for col in zip(*operand_2.lst)])
                return res_mtrx
            else:
                raise MatrixSizeError()
        else:
            raise TypeError()

    def transpose(self):
        return Matrix(list(map(list, zip(*self.lst))))

    def tr(self):
        row, col = self.size()
        if row == col:
            summa = 0
            for i in range(row):
                summa += self.lst[i][i]
            return summa
        else:
            raise MatrixSizeError()

    def det(self):
        row, col = self.size()
        if row == col:
            if row == 1:
                return self.lst[0][0]
            elif row == 2:
                return (self.lst[0][0] * self.lst[1][1] -
                        self.lst[0][1] * self.lst[1][0])
            tmp = [row for k, row in enumerate(self.lst) if k != 0]
            return sum((-1) ** j *
                       self.lst[0][j] *
                       Matrix([col for k, col in enumerate(zip(*tmp))
                              if k != j]).det() for j in range(row))
        else:
            raise MatrixSizeError()
