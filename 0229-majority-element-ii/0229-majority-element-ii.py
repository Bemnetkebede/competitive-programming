class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        c = Counter(nums)
        res = []
        for key , value in c.items():
            if value > n/3:
                res.append(key)
        return res
        
        