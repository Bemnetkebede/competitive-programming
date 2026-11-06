class Solution(object):
    def numberOfPairs(self, nums):
        left_over = 0
        pair = 0
        c = Counter(nums)
        for value in c.values():
            if value % 2  == 0:
               pair += value // 2
            else:
                pair += value // 2
                left_over += value % 2 
        return [pair , left_over]