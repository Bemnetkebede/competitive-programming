class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt = 0
        swap = 0
        for i in range(len(s)):
            if s[i] == '1':
                cnt += 1
            else:
                swap += cnt
        return swap


        