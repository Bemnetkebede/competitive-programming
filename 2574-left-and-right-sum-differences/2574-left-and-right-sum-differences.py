class Solution(object):
    def leftRightDifference(self, nums):
        totalSum = sum(nums)  
        leftSum = 0  
        result = []  
        for i in range(len(nums)):
            rightSum = totalSum - leftSum - nums[i]
            result.append(abs(leftSum - rightSum)) 
            leftSum += nums[i]

        return result  
            