class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        cnt_less = 0
        cnt_equ = 0
        for i in range(len(nums)):
            if nums[i] < target:
                cnt_less += 1
            elif nums[i] == target:
                cnt_equ += 1
        res  = []
        for i in range(cnt_less, cnt_less+cnt_equ):
                res.append(i)
        return res
                