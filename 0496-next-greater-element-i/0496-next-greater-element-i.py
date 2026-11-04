class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = [-1] * len(nums1)
        
        for i in range(len(nums1)):
            curr_num = nums1[i]
            
            idx_in_nums2 = nums2.index(curr_num)
            
            for j in range(idx_in_nums2 + 1, len(nums2)):
                if nums2[j] > curr_num:
                    result[i] = nums2[j]
                    break 
                    
        return result