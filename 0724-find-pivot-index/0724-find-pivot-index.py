class Solution(object):
    def pivotIndex(self, nums):
       total=sum(nums)
       leftSum=0
       for i in range(len(nums)):
           rightSum=total-nums[i]-leftSum
           if rightSum==leftSum:
               return i
           leftSum+=nums[i]
           
       return -1





       