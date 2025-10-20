# CSE304-2025-2-Algorithms
# Week05-3.2.bin2_problem.py

def bin2(n, k):
    B = [[0] * (k + 1) for _ in range(n + 1)] # n은 행개수 k는 열개수
    # Complete the code here
    for i in range(n+1):
        for j in range(min(i,k) + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]

    return B[n][k]


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_binomial(n, k, expected):
    print(f"Before computation: n = {n}, k = {k}")
    result = bin2(n, k)
    print(f"After computation: result = {result}")
    
    if result == expected:
        print("✅Test Passed!")
    else:
        print("❌Test Failed!")
        print(f"Expected result: {expected}")
        print(f"Your Result: {result}")
    print("-" * 40)


print("**************Testing bin2()**************")
print("######Example 1######")
test_binomial(15, 7, 6435)

print("######Example 2######")
test_binomial(30, 10, 30045015)

print("######Example 3######")
test_binomial(40, 20, 137846528820)

print("######Example 4######")
test_binomial(100, 0, 1)

print("######Example 5######")
test_binomial(100, 50, 100891344545564193334812497256)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 6 (Custom)
# test_binomial(n, k, expected)
