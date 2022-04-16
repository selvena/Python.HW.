
m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [[8, 3, 7, 1], [3, 5, 8, 3], [2, 4, 6, 7]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists
    def __str__(self):
        return '\n'.join(map(str, self.lists))
    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
            return '\n'.join(map(str, c))

matrix_1 = Matrix(m_1)
matrix_2 = Matrix(m_2)
print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix_2}\n{'-' * 20}")
print(f"matrix 1 + matrix 2\n{matrix_1 + matrix_2}")