class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        my_set = set()
        path = []
        def helper():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for j in range(len(nums)):
                if j in my_set:
                  continue
                my_set.add(j)
                path.append(nums[j])
                helper()
                path.pop()
                my_set.remove(j)
               
        helper()
        return res


        