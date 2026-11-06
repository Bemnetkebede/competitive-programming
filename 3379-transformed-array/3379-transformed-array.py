class Solution(object):
    def constructTransformedArray(self, nums):
        result = []
        n = len(nums)
        for idx , num in enumerate(nums):
            if num > 0:
                result.append(nums[(idx + num) % n]) 
            elif num < 0:
                result.append(nums[(idx + num) % n]) 
            else:
                result.append(num)
        return result   
        
        