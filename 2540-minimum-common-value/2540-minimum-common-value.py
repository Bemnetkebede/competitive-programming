class Solution(object):
    def getCommon(self, nums1, nums2):
        seen=set(nums1)
        minimum = float('inf') 
        for i in nums2:
            if i in seen:
               minimum = min(minimum , i)
        return minimum if minimum != float('inf') else -1
        