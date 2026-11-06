class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower(nums , target):
            low , high = 0 , len(nums)-1
            while low <=  high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            if low < len(nums) and nums[low] == target:
                return low
            return -1 
        def upper(nums , target):
            low , high = 0 , len(nums)-1
            while low <=  high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            if high >= 0  and nums[high] == target:
                return high
            else:
                return -1
        return [(lower(nums , target)) ,(upper(nums , target)) ]
         

        