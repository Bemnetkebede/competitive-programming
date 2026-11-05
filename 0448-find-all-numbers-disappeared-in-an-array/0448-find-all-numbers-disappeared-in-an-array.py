class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        nu = set(nums)
        for i in range(1, len(nums)+1):
            if i not in nu:
                res.append(i)
        return res
        