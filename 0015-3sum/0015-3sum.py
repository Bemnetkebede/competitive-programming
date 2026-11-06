class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Sort the array first
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    
                    # Skip duplicates for the second element
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    
                    # Skip duplicates for the third element
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        
        return result
