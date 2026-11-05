class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * len(nums)
        stack = []
        for i in range(2 * n):
            while stack and stack[-1][1] < nums[i % n]:
                stackIdx , stackNum = stack.pop()
                res[stackIdx] = nums[i % n]
            stack.append([i%n , nums[i%n]])
        return res
            