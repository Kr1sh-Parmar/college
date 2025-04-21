
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def multiply(self, other):
        result = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                result[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(3))
        return Matrix(result)

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
    


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)


print("\nAddition of Matrix 1 and Matrix 2:")
print(matrix1.add(matrix2))


print("\nMultiplication of Matrix 1 and Matrix 2:")
print(matrix1.multiply(matrix2))


print("\nTranspose of Matrix 1:")
print(matrix1.transpose())

print("\nTranspose of Matrix 2:")
print(matrix2.transpose())


