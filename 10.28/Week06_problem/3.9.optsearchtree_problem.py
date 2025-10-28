# CSE304-2025-2-Algorithms
# Week05-3.9.optsearchtree_problem.py

def minimum(i, j, M, p):
    minvalue, mink = INF, 0
    for k in range(i, j + 1):
        # Complete the code here
        current_value = M[i][k-1] + M[k+1][j]

        if current_value < minvalue:
            minvalue = current_value
            mink = k
            
    return minvalue, mink 

def optsearchtree(n, p):
    # Complete the code here
    # Tip: Implement minimum() and use it

    M = [[INF] * (n + 2) for _ in range(n + 2)]
    R = [[0] * (n + 2) for _ in range(n + 2)]
    W = [[0] * (n + 2) for _ in range(n + 2)]

    for i in range(1, n + 2):
        M[i][i-1] = 0
        W[i][i-1] = 0

    for i in range(1, n + 1):
        M[i][i] = p[i]
        W[i][i] = p[i]

    for diagonal in range(1, n + 1):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            if j < len(p): # p 배열의 길이를 초과하지 않도록 검사
                W[i][j] = W[i][j-1] + p[j]
    
    for length in range(2, n + 2):
        for i in range(1, n - length + 3):
            j = i + length - 1
            if j > n: continue

            min_cost, k = minimum(i, j, M, p)
            
            M[i][j] = min_cost + W[i][j]
            R[i][j] = k
    
    return M[1][n], M, R


INF = float("inf")

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_optsearchtree(p, expected_minavg=None, expected_R_partial=None):
    print("Before computation")
    print(f"p = {p[1:]}")

    n = len(p) - 1
    minavg, A, R = optsearchtree(n, p)

    print("After computation")
    print("R table:")
    for i in range(1, n + 1):
        print(f"R[{i}][{i}:] = {R[i][i:n+1]}")

    print("Minimum expected cost:", minavg)

    if expected_minavg is not None:
        if abs(minavg - expected_minavg) < 1e-6:
            print("✅Test Passed! (minimum expected cost matches)")
        else:
            print("❌Test Failed!")
            print(f"Expected result: {expected_minavg}")
            print(f"Your Result: {minavg}")

    if expected_R_partial is not None:
        for i, j, expected_val in expected_R_partial:
            actual = R[i][j]
            if actual == expected_val:
                print(f"✅ R[{i}][{j}] = {actual} (Correct)")
            else:
                print(f"❌ R[{i}][{j}] = {actual}, Expected = {expected_val}")

    print("-" * 40)
    return minavg


print("**************Testing optsearchtree()**************")

print("######Example 1######")
p1 = [0, 0.375, 0.375, 0.125, 0.125]
expected_minavg1 = 1.75
expected_R1 = [
    (1, 1, 1),
    (1, 2, 1),
    (1, 3, 2),
    (1, 4, 2)
]
test_optsearchtree(p1, expected_minavg1, expected_R1)

print("######Example 2######")
p2 = [0, 0.7, 0.1, 0.1, 0.1]
expected_minavg2 = 1.5
expected_R2 = [
    (1, 1, 1),
    (1, 2, 1),
    (1, 3, 1),
    (1, 4, 1)
]
test_optsearchtree(p2, expected_minavg2, expected_R2)

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 3 (Custom)
# test_optsearchtree(p, expected_minavg, expected_R_partial)