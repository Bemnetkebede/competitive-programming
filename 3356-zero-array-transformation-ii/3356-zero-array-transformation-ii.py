class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def checker(mid):
            res = [0] * (len(nums) + 1)
            for i in range(mid+1):
                l , r , val = queries[i]
                res[l] += val
                if r + 1 < len(res):
                   res[r + 1] -= val
            for k in range(1 , len(res)):
                res[k] += res[k-1]
            for j in range(len(nums)):
                if nums[j] - res[j] > 0:
                    return False
            return True
        if all(num == 0 for num in nums):
            return 0
        low , high = 0 , len(queries)-1
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if checker(mid):
                ans = mid + 1
                high = mid-1
            else:
                low = mid + 1
        return ans


        