from collections import Counter
class Solution(object):
    def getSneakyNumbers(self, nums):
        res = []
        c = Counter(nums)
        for key ,value in c.items():
            if value > 1:
                res.append(key)
        return res



        