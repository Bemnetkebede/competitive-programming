class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()
        small = []
        l , r = 0 , len(nums)-1
        while l < r :
            average = float(nums[l] + nums[r])
            average = float(average/2)
            small.append(average)
            l += 1
            r -= 1
        return min(small)
        
        
