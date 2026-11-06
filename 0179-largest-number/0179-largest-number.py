class Solution(object):
    def largestNumber(self, nums):
        res = ''
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if str(nums[j]) + str(nums[j+1]) < str(nums[j+1]) + str(nums[j]):
                    nums[j] , nums[j+1] = nums[j+1] , nums[j] 
                      
        for k in nums:
            res +=str(k) 
        return "0" if res[0] == "0" else res  

                

    








        

            


        
        
       
                