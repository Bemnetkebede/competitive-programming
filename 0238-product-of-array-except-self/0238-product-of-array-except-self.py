class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        suffix = [] 
        p = 1
        for i in range(len(nums)):
            p *=  nums[i]
            prefix.append(p)
        print(prefix)
        p = 1
        for j in range(len(nums)-1,-1,-1):
            p *=  nums[j]
            suffix.append(p)
        suffix = suffix[::-1]
        for k in range(len(nums)):
            if k == 0:
                res.append(suffix[k+1]) 
            elif k == len(nums) - 1:
                res.append(prefix[k-1])
            else:
                res.append(prefix[k-1] * suffix[k+1]) 
        return res

            
        


        