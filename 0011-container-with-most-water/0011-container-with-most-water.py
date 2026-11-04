class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_val = 0
        while l < r:
            max_val = max(max_val , (r - l) * min(height[r] , height[l]))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1 
        return max_val


        