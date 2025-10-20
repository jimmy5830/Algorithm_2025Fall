# CSE304-2025-2-Algorithms
# Week03-leetcode_215_problem.py
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

from typing import List

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def mergeSort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left_half = mergeSort(arr[:mid])
            right_half = mergeSort(arr[mid:])
            
            return merge(left_half, right_half)
        
        def merge(left: List[int], right: List[int]) -> List[int]:
            merged_list = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged_list.append(left[i])
                    i += 1
                else:
                    merged_list.append(right[j])
                    j += 1
            
            merged_list.extend(left[i:])
            merged_list.extend(right[j:])
            
            return merged_list
        
        sorted_nums = mergeSort(nums)
        
        return sorted_nums[len(sorted_nums) - k]

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_findKthLargest(nums, k, expected_result):
    solution = Solution()
    result = solution.findKthLargest(nums, k)
    
    if result == expected_result:
        print(f"Test Passed!")
    else:
        print(f"Test Failed!")
    
    n = len(nums)
    if n > 20:
        preview = (
            "[" +
            ", ".join(map(str, nums[:10])) +
            ", ... , " +
            ", ".join(map(str, nums[-10:])) +
            "]"
        )
        print(f"Input array: (showing first/last 10 elements)")
        print(preview)
    else:
        print(f"Input array: {nums}")
    
    print(f"k: {k}")
    print(f"Expected result: {expected_result}")
    print(f"Your Result: {result}")
    print("-" * 40)

if __name__ == "__main__":
    print("######Example 1######")
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    test_findKthLargest(nums1, k1, 5)
    
    print("######Example 2######")
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    test_findKthLargest(nums2, k2, 4)
    
    print("######Example 3######")
    nums3 = [-500] * 90000 + [1000] * 10000
    k3 = 10000
    test_findKthLargest(nums3, k3, 1000)
    
    print("######Example 4######")
    nums4 = [-10000, 10000, -5000, 5000, 0, 9999, -9999]
    k4 = 1
    test_findKthLargest(nums4, k4, 10000)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 5 (Custom)
# nums5 = []
# k5 =
# test_findKthLargest(nums5, k5, expected_result)