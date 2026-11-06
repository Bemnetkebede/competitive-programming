class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_L = 0
        count_R = 0
        c = 0
        for i , s in enumerate(s):
            if s == 'R':
                count_R += 1
            else:
                count_L += 1
            if count_R == count_L:
                c += 1
                count_L = 0
                count_R = 0
        return c
                



        