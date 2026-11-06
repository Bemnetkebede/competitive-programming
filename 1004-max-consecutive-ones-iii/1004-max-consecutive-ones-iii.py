class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
               zeros += 1
            while k < zeros:
                if nums[l] != 0:
                    l += 1
                else:
                    zeros -= 1
                    l += 1
            print(l , i)
            count = max(count , i-l + 1)
        return count 
                

                
        #     temp = k
        #     if nums[i] == 1:
        #         continue
        #     elif temp > 0:
        #        if nums[i] == 0:
        #         k -= 1
        #     elif nums[i] == 0 and temp == 0:
        #         l += 1
        #     count = max(count , i - l +1 )
        # return count





        