class Solution(object):
    def sortArray(self, nums):
        max_num = max(nums)
        min_val = min(nums)
        res =  [0] * (max_num - min_val + 1)
        for num in nums:
            res[num - min_val] += 1   
        la = []    
        for i in range(len(res)):
            if res[i] >= 1:
               for j in range(res[i]):
                   la.append(i + min_val)
        return la
    