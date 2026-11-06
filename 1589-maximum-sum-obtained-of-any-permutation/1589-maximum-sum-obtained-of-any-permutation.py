class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        req = [0] * (n+1)
        for start , end in requests:
            req[start] += 1
            req[end+1] -= 1
        for i in range(1 , len(req)):
            req[i] = req[i] + req[i-1]
        
        req.sort(reverse=True)
        nums.sort(reverse=True)
         
        result = 0
        for i in range(len(nums)):
            result += nums[i] * req[i]

        return result % (10 ** 9 +7)



            

        