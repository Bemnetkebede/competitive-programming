class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n = len(nums)
        print(n)
        cnt = 0
        while n >= 2 and nums[0] < k:
            x  = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums ,(min(x, y) * 2 + max(x, y)))
            cnt += 1
        return cnt

        