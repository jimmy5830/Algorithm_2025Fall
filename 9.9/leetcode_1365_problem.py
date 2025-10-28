class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        list = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] > nums[j]:
                        counter += 1
            list.append(counter)
        return list
        


        