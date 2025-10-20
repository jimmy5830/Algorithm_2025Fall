# CSE304-2025-2-Algorithms
# Week04-2.8.strassen_problem.py

class Matrix:
    def __init__(self, mat):
        self.n = len(mat)
        self.matrix = mat
    
    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.n)] for i in range(self.n)])
    
    def __sub__(self, other):
        return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(self.n)] for i in range(self.n)])
    
    def __mul__(self, other):
        mat = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    mat[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(mat)
    
    def __str__(self):  
        return "\n".join(" ".join(f"{val:5}" for val in row) for row in self.matrix)

    __repr__ = __str__


def partition(n, M):
    m = n // 2
    m1 = [[0] * m for _ in range(m)]
    m2 = [[0] * m for _ in range(m)]
    m3 = [[0] * m for _ in range(m)]
    m4 = [[0] * m for _ in range(m)]

    A = M.matrix
    for i in range(m):
        for j in range(m):
            # Complete the code here
            m1[i][j] = A[i][j]
            m2[i][j] = A[i][j + m]
            m3[i][j] = A[i + m][j]
            m4[i][j] = A[i + m][j + m]

    return Matrix(m1), Matrix(m2), Matrix(m3), Matrix(m4)


def combine(n, M1, M2, M3, M4):
    m = n // 2
    mat = [[0] * n for _ in range(n)]

    A = M1.matrix  
    B = M2.matrix  
    C = M3.matrix  
    D = M4.matrix  

    for i in range(m):
        for j in range(m):
            mat[i][j]       = A[i][j]
            mat[i][j + m]   = B[i][j]
            mat[i + m][j]   = C[i][j]
            mat[i + m][j+m] = D[i][j]

    return Matrix(mat)


def strassen(n, A, B):
    global threshold

    if n <= threshold:
        return A * B
    else:
        A11, A12, A21, A22 = partition(n, A)
        B11, B12, B21, B22 = partition(n, B)

        m = n // 2

        ms1 = strassen(m, A11 + A22, B11 + B22)
        ms2 = strassen(m, A21 + A22, B11)
        ms3 = strassen(m, A11,       B12 - B22)
        ms4 = strassen(m, A22,       B21 - B11)
        ms5 = strassen(m, A11 + A12, B22)
        ms6 = strassen(m, A21 - A11, B11 + B12)     
        ms7 = strassen(m, A12 - A22, B21 + B22)

        C11 = ms1 + ms4 - ms5 + ms7
        C12 = ms3 + ms5
        C21 = ms2 + ms4
        C22 = ms1 + ms3 - ms2 + ms6

        return combine(n, C11, C12, C21, C22)


threshold = 1

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_strassen(A_matrix, B_matrix):    
    A = Matrix(A_matrix)
    B = Matrix(B_matrix)
    
    n = len(A_matrix)
    
    expected = A * B
    
    strassen_result = strassen(n, A, B)
    
    is_correct = all(strassen_result.matrix[i][j] == expected.matrix[i][j] 
                    for i in range(n) for j in range(n))
    
    if is_correct:
        print("✅Test Passed!")
    else:
        print(f"❌Test Failed!")
    print(f"Expected result: \n{expected}")
    print(f"Your Result: \n{strassen_result}")
    
    print("-" * 40)


if __name__ == "__main__":
    A1 = [[1, 2], [3, 4]]
    B1 = [[5, 6], [7, 8]]
    print("######Example 1######")
    test_strassen(A1, B1)
    
    A2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]]
    B2 = [[8, 9, 1, 2], [3, 4, 5, 6], [7, 8, 9, 1], [2, 3, 4, 5]]
    print("######Example 2######")
    test_strassen(A2, B2)

    A3 = [
        [12, 8, 4, 0, 9, 6, 2, 7],
        [1, 5, 10, 3, 11, 15, 4, 8],
        [7, 13, 2, 9, 0, 5, 10, 14],
        [3, 6, 1, 8, 12, 4, 7, 2],
        [9, 4, 11, 5, 3, 8, 1, 6],
        [13, 0, 7, 10, 2, 14, 5, 9],
        [6, 12, 3, 15, 7, 1, 13, 4],
        [8, 2, 10, 4, 6, 11, 9, 0]
    ]
    
    B3 = [
        [5, 3, 8, 10, 1, 7, 4, 9],
        [11, 2, 6, 4, 13, 0, 8, 5],
        [3, 9, 1, 7, 12, 6, 2, 10],
        [14, 0, 5, 11, 8, 3, 7, 2],
        [4, 10, 2, 6, 9, 13, 1, 8],
        [7, 12, 15, 3, 0, 5, 11, 4],
        [9, 5, 10, 2, 7, 4, 6, 12],
        [1, 8, 4, 13, 3, 9, 0, 6]
    ]
    print("######Example 3######")
    test_strassen(A3, B3)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 4 (Custom)
# A4 = [[], []]
# B4 = [[], []]
# test_strassen(A4, B4)