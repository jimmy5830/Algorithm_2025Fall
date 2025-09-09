class Solution(object):
    def runningSum(self, nums):
        Sum = 0
        answer = []

        for n in nums:
            Sum += n
            answer.append(Sum)

        return answer
        