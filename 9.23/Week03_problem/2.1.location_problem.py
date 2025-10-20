# CSE304-2025-2-Algorithms
# Week03-2.1.location_problem.py

def location(low, high, S, x):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if (x == S[mid]):
            return mid
        elif(x < S[mid]):
            return location(low, mid-1, S, x)
        else:
            return location(mid+1, high, S, x)
        
        # Complete the code here

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_case(S, x, expected_result):
    result = location(0, len(S)-1, S, x)
    
    if result == expected_result:
        print("Test Passed!")
    else:
        print(f"Test Failed!")
    print(f"Input array: {S}")
    print(f"Search value: {x}")
    print(f"Expected result: {expected_result}")
    print(f"Your Result: {result}")
    print("-" * 40)


if __name__ == "__main__":
    print("######Example 1######")
    S = [5, 7, 8, 10, 11, 13]
    x = 15 
    expected_result = -1
    test_case(S, x, expected_result)
    
    print("######Example 2######") 
    S = [5, 7, 8, 10, 11, 13]
    x = 10 
    expected_result = 3
    test_case(S, x, expected_result)
    
    print("######Example 3######") 
    S = [5, 7, 8, 10, 11, 13]
    x = 5
    expected_result = 0
    test_case(S, x, expected_result)
    
    print("######Example 4######") 
    S = [5, 7, 8, 10, 11, 13]
    x = 13
    expected_result = 5
    test_case(S, x, expected_result)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 5 (Custom)
# S = []
# x = 
# expected_result =
# test_case(S, x, expected_result)