# CSE304-2025-2-Algorithms
# Week02-1.7.fib2_problem.py
import time

def fib2(n):
    # Complete the code here
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    a, b = 1, 1   # F(1), F(2)
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def fib_expected(n):
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b if n > 0 else 0

def test_case(n, expected_result):
    stime = time.time()
    result = fib2(n)
    etime = time.time() - stime
    
    if result == expected_result:
        print("Test Passed!")
    else:
        print("Test Failed!")
    print(f"Input value: {n}")
    print(f"Execution time: {round(etime, 5)}s")
    print(f"Expected result: {expected_result}")
    print(f"Your Result: {result}")
    print("-" * 40)

print("######Example 1######")
n = 30
expected_result = fib_expected(n)
test_case(n, expected_result)

print("######Example 2######") 
n = 36
expected_result = fib_expected(n)
test_case(n, expected_result)

print("######Example 3######") 
n = 40
expected_result = fib_expected(n)
test_case(n, expected_result)

print("######Example 4######") 
n = 0
expected_result = fib_expected(n)
test_case(n, expected_result)

print("######Example 5######") 
n = 1
expected_result = fib_expected(n)
test_case(n, expected_result)

print("######Example 6######") 
n = 1000
expected_result = fib_expected(n)
test_case(n, expected_result)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 7 (Custom)
# n = 
# expected_result = fib_expected(n)
# test_case(n, expected_result)