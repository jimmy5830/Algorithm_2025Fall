# CSE304-2025-2-Algorithms
# Week03-baekjoon_17829_problem.py
# https://www.acmicpc.net/problem/17829

class Solution:
    def pooling(self, matrix, x, y, n): 

        if n == 1:
            return matrix[x][y]
        
        half = n // 2
        
        top_left = self.pooling(matrix, x, y, half)
        top_right = self.pooling(matrix, x, y + half, half)
        bottom_left = self.pooling(matrix, x + half, y, half)
        bottom_right = self.pooling(matrix, x + half, y + half, half)

        values = [top_left, top_right, bottom_left, bottom_right]
        values.sort()
        
        return values[-2]

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_pooling(matrix, expected_result):
    n = len(matrix)
    solution = Solution()
    result = solution.pooling(matrix, 0, 0, n)
    
    if result == expected_result:
        print(f"Tast Passed!")
    else:
        print(f"Test Failed!")
    
    print(f"Input Matrix Size: {n}x{n} (N=2^{n.bit_length()-1})")
    
    if n > 8:
        print("Input Matrix (too large, showing partial):")
        for i in range(min(4, n)):
            print(" ".join(map(str, matrix[i][:4])) + " ... " + " ".join(map(str, matrix[i][-4:])))
        print("...")
        for i in range(max(0, n-4), n):
            print(" ".join(map(str, matrix[i][:4])) + " ... " + " ".join(map(str, matrix[i][-4:])))
    else:
        print("Input Matrix:")
        for row in matrix:
            print(" ".join(map(str, row)))
    
    print(f"Result: {result}")
    print("-" * 40)



if __name__ == "__main__":
    print("######Example 1######") 
    matrix1 = [
        [-6, -8, 7, -4],
        [-5, -5, 14, 11],
        [11, 11, -1, -1],
        [4, 9, -2, -4]
    ]
    test_pooling(matrix1, 11)
    
    print("######Example 2######") 
    matrix2 = [
        [-1, 2, 14, 7, 4, -5, 8, 9],
        [10, 6, 23, 2, -1, -1, 7, 11],
        [9, 3, 5, -2, 4, 4, 6, 6],
        [7, 15, 0, 8, 21, 20, 6, 6],
        [19, 8, 12, -8, 4, 5, 2, 9],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24]
    ]
    test_pooling(matrix2, 17)
    
    print("######Example 3######") 
    matrix3 = [
        [-7, -9, 8, -5],
        [-6, -6, 15, 12],
        [12, 12, -2, -2],
        [5, 10, -3, -5]
    ]
    test_pooling(matrix3, 12)
    
    print("######Example 4 (Minimum Size N=2)######") 
    matrix4 = [
        [-10000, 10000],
        [10000, -10000]
    ]
    test_pooling(matrix4, 10000)

    print("######Example 5 (Maximum Size N=1024)######") 
    matrix5 = []
    for i in range(1024):
        row = []
        for j in range(1024):
            if (i + j) % 3 == 0:
                value = 10000
            elif (i + j) % 3 == 1:
                value = -10000 
            else:
                value = (i * j) % 10000 - 5000
            row.append(value)
        matrix5.append(row)
    solution = Solution()
    expected_result5 = solution.pooling(matrix5, 0, 0, 1024)
    test_pooling(matrix5, expected_result5)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 6 (Custom)
# matrix6 = []
# test_pooling(matrix6, ...)