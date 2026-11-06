class Solution(object):
    def reversePairs(self, nums):
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums, 0
            
            mid = len(nums) // 2
            left, left_count = merge_sort(nums[:mid])
            right, right_count = merge_sort(nums[mid:])
            
            # Count reverse pairs
            count = left_count + right_count
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > right[j] * 2:
                    j += 1
                count += j  # All elements from right[0] to right[j-1] are valid pairs with left[i]
            
            # Merge the two halves
            merged = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            # Add any remaining elements
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            return merged , count
        
        _, total_count = merge_sort(nums)
        return total_count
