from simplex_method import Simplex
import numpy as np

def test_simplex():
    input_array = np.array([[25, -3, 5], [30, -2, 5], [10, 1, 0], [6, 3, -8], [0, -6, -5]])

    result = []
    s = Simplex(input_array)
    table_result = s.calculate(result)

    print('Решённая симплекс-таблица:')
    print(table_result)

    print()
    print("Решение: ")
    print(result)

if __name__ == '__main__':
    test_simplex()