'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
'''


class Matrix:
    def __init__(self, list1):
        self._matrix = list1

        m_rows = len(self._matrix)
        self._matrix_size = frozenset([(m_rows, len(row)) for row in self._matrix])

        if len(self._matrix_size) != 1:
            raise ValueError("Invalid matrix size")

    def __add__(self, other: "Matrix"):

        result = []
        for item in zip(self._matrix, other._matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self._matrix])


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2], [3, 4]])
    print(matrix1, '\n')

    matrix2 = Matrix([[10, 20], [30, 40]])
    print(matrix2, '\n')

    print(matrix1 + matrix2)


