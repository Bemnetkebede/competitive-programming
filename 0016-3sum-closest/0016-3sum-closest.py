class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = sum(nums[:3])
        for i in range(len(nums)):
            l = i+1 
            r = n-1 
            temp = target - nums[i]        
            while l < r:
                su = nums[l] + nums[r]
                ans = min(ans, su + nums[i], key = lambda x: abs(x - target))
                if su < temp:
                    l += 1
                elif su > temp:
                    r -= 1
                else:
                    break
        return ans
