class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def helper(i, path):
            arr.append(path.copy())
            for j in range(i, len(nums)):
                path.append(nums[j])
                helper(j+1 , path)
                path.pop()
        helper(0 , [])
        return arr