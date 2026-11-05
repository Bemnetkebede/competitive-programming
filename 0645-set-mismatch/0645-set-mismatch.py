class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mx = Counter(nums)
        res = []
        for idx , val in mx.items():
            if val >= 2:
                res.append(idx)
        for i in range(1 , len(nums)+1):
            if i not in nums:
                res.append(i)
        return res
