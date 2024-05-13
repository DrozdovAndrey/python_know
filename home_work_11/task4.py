# Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.
#
# Атрибуты класса:
#
# rows (int): Количество строк в матрице.
# cols (int): Количество столбцов в матрице.
# data (list): Двумерный список, содержащий элементы матрицы.
#
# Методы класса:
#
# __init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols, а также создает двумерный
# список data размером rows x cols и заполняет его нулями.
#
# __str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу, где
# элементы разделены пробелами, а строки разделены символами новой строки. Например:
#
#
# 1 2 3
# 4 5 6
# __repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано для создания
# нового объекта того же класса с такими же размерами и данными.
#
# __eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True,
# если они имеют одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False.
#
# __add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют одинаковые
# размеры (количество строк и столбцов). Если размеры совпадают, создает новую матрицу, где каждый элемент равен сумме
# соответствующих элементов входных матриц.
#
# __mul__(self, other): Метод, определяющий операцию умножения двух матриц. Проверяет, что количество столбцов в первой
# матрице равно количеству строк во второй матрице. Если условие выполняется, создает новую матрицу, где элемент на
# позиции [i][j] равен сумме произведений элементов соответствующей строки из первой матрицы и столбца из второй
# матрицы.
class Matrix:
    """
      Класс, представляющий матрицу.

      Атрибуты:
      - rows (int): количество строк в матрице
      - cols (int): количество столбцов в матрице
      - data (list): двумерный список, содержащий элементы матрицы

      Методы:
      - __str__(): возвращает строковое представление матрицы
      - __repr__(): возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта
      - __eq__(other): определяет операцию "равно" для двух матриц
      - __add__(other): определяет операцию сложения двух матриц
      - __mul__(other): определяет операцию умножения двух матриц
      """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = self.create_matrix()
        # self.data = [[0 for j in range(cols)] for i in range(rows)]

    def create_matrix(self):
        """
        Создает матрицу по заданным размерам и заполняет ее 0

        :return: матрицу размером rows * cols
        """
        lst = []
        for i in range(self.rows):
            lst.append([0 for _ in range(self.cols)])
        return lst

    def __str__(self):
        """
           Возвращает строковое представление матрицы.

           Возвращает:
           - str: строковое представление матрицы
        """
        str_matr = ''
        for i in range(self.rows):
            for j in range(self.cols):
                if j != self.cols - 1:
                    str_matr += f'{self.data[i][j]} '
                else:
                    str_matr += f'{self.data[i][j]}'
            if i != self.rows - 1:
                str_matr += '\n'
        return str_matr
        # return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])

    def __repr__(self):
        """
        Возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление матрицы
        """
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - bool: True, если матрицы равны, иначе False
        """
        if self.rows == other.rows and self.cols == other.cols:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.data[i][j] != other.data[i][j]:
                        return False
            return True

    def __add__(self, other):
        """
        Определяет операцию сложения двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - Matrix: новая матрица, полученная путем сложения двух исходных матриц
        """
        if self.rows == other.rows and self.cols == other.cols:
            sum_matrix = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    sum_matrix.data[i][j] = self.data[i][j] + other.data[i][j]
            return sum_matrix

    def __mul__(self, other):
        """
        Определяет операцию умножения двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - Matrix: новая матрица, полученная путем умножения двух исходных матриц
        """
        if self.cols == other.rows:
            mult_matrix = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        mult_matrix.data[i][j] += self.data[i][k] * other.data[k][j]
            return mult_matrix


matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

print(matrix1 == matrix2)

matrix_sum = matrix1 + matrix2
print(matrix_sum)

matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2],
                [3, 4],
                [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8],
                [9, 10]]

result = matrix3 * matrix4
print(result)
