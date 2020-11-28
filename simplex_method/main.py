from simplex_method import Simplex
import numpy as np

def test_simplex():

    # ИЩЕМ МАКСИМУМ: -F(X), ИЩЕМ МИНИМУМ: F(X)
    # ЦЕЛЕВАЯ ФУНКЦИЯ В ПОСЛЕДНЕЙ СТРОКЕ МАТРИЦЫ
    # первый элемент в каждой строке - ограничение
    input_array = np.array([[55, 1, 1],
                            [120, 2, 3],
                            [960, 12, 30],
                            [0, -3, -4]])


    result = [0, 0]
    s = Simplex(input_array)
    table_result = s.calculate(result)

    print('Решённая симплекс-таблица:')
    print(table_result)

    print()
    print("Решение: ")
    print(result)

if __name__ == '__main__':
    test_simplex()