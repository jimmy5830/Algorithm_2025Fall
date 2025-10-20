# CSE304-2025-2-Algorithms
# Week05-3.4.floyd2_problem.py

def floyd2(n, W):
    P = [[-1] * n for _ in range(n)]
    D = [row[:] for row in W]
    # Complete the code here
    for k in range(n):
        for i in range(n):
            for j in range(n):

                if D[i][k] != INF and D[k][j] != INF:
                    new_distance = D[i][k] + D[k][j]

                    if new_distance < D[i][j]:
                        D[i][j] = new_distance

                        P[i][j] = k

    return D, P


def path(i, j):
    k = P[i][j]
    if k != -1:
        path(i, k)
        print("v" + str(k), end=" ")
        path(k, j)


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_floyd(n, W, expected_D=None, path_start=None, path_end=None):
    print("Before Floyd-Warshall computation")
    global P
    D, P = floyd2(n, W)
    print("After computation (D and P):")

    print("D = ")
    for row in D:
        print(row)
    print("P = ")
    for row in P:
        print(row)

    if path_start is not None and path_end is not None:
        print(f"Path from v{path_start} to v{path_end}: ", end="")
        path(path_start, path_end)
        print()

    if expected_D is not None:
        correct = True
        for i in range(n):
            for j in range(n):
                if D[i][j] != expected_D[i][j]:
                    correct = False
                    print(f"Mismatch at D[{i}][{j}]: Expected {expected_D[i][j]}, got {D[i][j]}")
        if correct:
            print("✅Test Passed!")
        else:
            print("❌Test Failed!")
    print("-" * 40)


INF = float("inf")

print("**************Testing floyd2()**************")

print("######Example 1######")
n1 = 5
W1 = [
    [0, 1, INF, 1, 5],
    [9, 0, 3, 2, INF],
    [INF, INF, 0, 4, INF],
    [INF, INF, 2, 0, 3],
    [3, INF, INF, INF, 0]
]
expected_D1 = [
    [0, 1, 3, 1, 4],
    [8, 0, 3, 2, 5],
    [10, 11, 0, 4, 7],
    [6, 7, 2, 0, 3],
    [3, 4, 6, 4, 0]
]
test_floyd(n1, W1, expected_D1, 4, 2)

print("######Example 2######")
n2 = 4
W2 = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]
expected_D2 = [
    [0, 3, 5, 6],
    [5, 0, 2, 3],
    [3, 6, 0, 1],
    [2, 5, 7, 0]
]
test_floyd(n2, W2, expected_D2, 0, 2)

print("######Example 3######")
n3 = 6
W3 = [
    [0, 6, INF, INF, INF, 8],
    [3, 0, 2, INF, INF, INF],
    [INF, INF, 0, 1, 7, INF],
    [INF, INF, INF, 0, 2, INF],
    [INF, 4, INF, INF, 0, 5],
    [INF, INF, INF, 4, 6, 0]
]
expected_D3 = [
    [0, 6, 8, 9, 11, 8],
    [3, 0, 2, 3, 5, 10],
    [10, 7, 0, 1, 3, 8],
    [9, 6, 8, 0, 2, 7],
    [7, 4, 6, 7, 0, 5],
    [13, 10, 12, 4, 6, 0]
]
test_floyd(n3, W3, expected_D3, 0, 4)

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 4 (Custom)
# test_floyd(n, W, expected_D, start, end)