class Solution(object):
    def separateDigits(self, nums):
        res = []
        for i in range(len(nums)):
            if len(str(nums[i])) > 1:
                for j in str(nums[i]):
                    res.append(int(j))
            else:
                res.append(nums[i])
        return res
        