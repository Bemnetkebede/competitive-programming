class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:  
            return 0

        product = 1  
        count = 0  
        l = 0 

        for i in range(len(nums)):  
            product *= nums[i]  

            while product >= k and l <= i:
                product //= nums[l]  
                l += 1 

            
            count += (i - l + 1)

        return count  


        