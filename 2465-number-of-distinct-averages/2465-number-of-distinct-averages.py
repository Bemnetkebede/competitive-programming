class Solution(object):
    def distinctAverages(self, nums):
        nums.sort()
        l = 0
        r = len(nums)-1
        average = set()
        while l < r:
            ave = float(nums[l] + nums[r])
            ave = float(ave/2)
            average.add(ave)
            l += 1
            r -= 1
        return len(average)
        