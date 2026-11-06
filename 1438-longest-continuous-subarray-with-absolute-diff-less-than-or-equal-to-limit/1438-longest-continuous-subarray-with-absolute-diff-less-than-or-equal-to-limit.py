from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_que = deque() 
        min_que = deque() 
        left = 0
        max_res = 0
        
        for right in range(len(nums)):
            num = nums[right]
           
            while max_que and max_que[-1] < num:
                max_que.pop()
            max_que.append(num)
            
            while min_que and min_que[-1] > num:
                min_que.pop()
            min_que.append(num)
            

            while max_que[0] - min_que[0] > limit:
                if max_que[0] == nums[left]:
                    max_que.popleft()
                if min_que[0] == nums[left]:
                    min_que.popleft()
                left += 1 # Shrink the window
                
 
            max_res = max(max_res, right - left + 1)
            
        return max_res
