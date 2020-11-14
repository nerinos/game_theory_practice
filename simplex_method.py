import numpy as np

class Simplex():
    def __init__(self, source):
        # source - симплекс таблица без базисных переменных
        self.source = source
        self.m = source.shape[0]
        self.n = source.shape[1]
        self.table = np.zeros([self.m, self.n + self.m - 1])
        self.basis = [] # список базисных переменных

        for i in range(0, self.m):
            for j in range(0, self.n):
                if (j < self.n):
                    self.table[i, j] = self.source[i, j]
            #         Выставляем коэффициент 1 перед базисной переменной в строке
            if (self.n + i) < self.table.shape[1]:
                self.table[i, self.n + i] = 1
                self.basis.append(self.n + i)
        self.n = self.table.shape[1]

    def is_ended(self):
        flag = True
        for i in range(0, self.n):
            if self.table[self.m - 1, i] < 0:
                flag = False
                break
        return flag

    # в этот массив будут записаны полученные значения X
    def calculate(self, result):
        while not self.is_ended():
            main_column = self.find_main_column()
            main_row = self.find_main_row(main_column)
            self.basis[main_row] = main_column
            new_table = np.zeros([self.m, self.n])
            for j in range(0, self.n):
                new_table[main_row, j] = self.table[main_row, j] / self.table[main_row, main_column]
            for i in range(0, self.m):
                if i == main_row:
                    continue
                for j in range(0, self.n):
                    new_table[i, j] = self.table[i, j] - self.table[i, main_column] * new_table[main_row, j]
            self.table = new_table

        for i in range(0, len(result)):
            k = self.basis.index(i + 1)
            if k != -1:
                result[i] = self.table[k, 0]
            else:
                result[i] = 0
        return self.table

    def find_main_column(self):
        main_column = 1

        for j in range(2, self.n):
            if self.table[self.m - 1, j] < self.table[self.m - 1, main_column]:
                main_column = j
        return main_column

    def find_main_row(self, main_column):
        main_row = 0

        for i in range(0, self.m - 1):
            if self.table[i, main_column] > 0:
                main_row = i
                break
        for i in range(main_row + 1, self.m):
            if self.table[i, main_column] > 0 and (self.table[i, 0] / self.table[i, main_column] < (self.table[main_row, 0] / self.table[main_row, main_column])):
                main_row = i
        return main_row
