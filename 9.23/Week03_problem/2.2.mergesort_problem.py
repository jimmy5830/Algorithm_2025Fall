# CSE304-2025-2-Algorithms
# Week03-2.2.mergesort_problem.py

def merge(h, m, U, V, S):
    i = j = k = 0
   
    while i < h and j < m:
        if U[i] < V[j]:
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1
        k += 1

  
    while i < h:
        S[k] = U[i]
        i += 1
        k += 1
    while j < m:
        S[k] = V[j]
        j += 1
        k += 1

def mergesort(n, S):
    if n > 1:
        h = n // 2
        m = n - h
        
        U = S[:h]
        V = S[h:]
        
        mergesort(h, U)
        mergesort(m, V)
        
        merge(h, m, U, V, S)
        # Complete the code here

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_merge(U, V, expected_result):
    h = len(U)
    m = len(V)
    S = [-1] * (h + m)
    
    merge(h, m, U, V, S)
    
    if S == expected_result:
        print(f"Test Passed!")
    else:
        print(f"Test Failed!")
    print(f"Input array U: {U}")
    print(f"Input array V: {V}")
    print(f"Expected result: {expected_result}")
    print(f"Your Result: {S}")
    print("-" * 40)

def test_mergesort(S, expected_result):
    original = S.copy()
    
    mergesort(len(S), S)
    
    if S == expected_result:
        print(f"Test Passed!")
    else:
        print(f"Test Failed!")
    print(f"Input array: {original}")
    print(f"Expected result: {expected_result}")
    print(f"Your Result: {S}")
    print("-" * 40)

print("######Example 1 for 'merge()'######")
U = [17, 19, 39, 41, 73]
V = [16, 22, 66, 94, 98]
expected_result = [16, 17, 19, 22, 39, 41, 66, 73, 94, 98]
test_merge(U, V, expected_result)

print("######Example 2 for 'merge()'######")
U = [1, 3, 5, 7, 9]
V = [2, 4, 6, 8, 10]
expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_merge(U, V, expected_result)

print("######Example 3 for 'mergesort()'######")
S = [22, 98, 17, 16, 19, 73, 94, 41, 39, 66]
expected_result = [16, 17, 19, 22, 39, 41, 66, 73, 94, 98]
test_mergesort(S, expected_result)

print("######Example 4 for 'mergesort()'######")
S = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
test_mergesort(S, expected_result)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 5 for 'merge()'(Custom)
# U = []
# V = []
# expected_result = []
# test_merge(U, V, expected_result)

# Example 6 for 'mergesort()'(Custom)
# S = []
# expected_result = []
# test_mergesort(S, expected_result)s