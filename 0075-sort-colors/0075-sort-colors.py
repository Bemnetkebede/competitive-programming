class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            j = i
            while nums[j-1] > nums[j] and j > 0:
                nums[j-1] , nums[j] = nums[j] , nums[j-1]
                j -= 1
        return nums

      

   
