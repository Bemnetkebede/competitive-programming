class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(math.prod(nums[-3:]),prod([nums[0],nums[1] , nums[-1]]))
        