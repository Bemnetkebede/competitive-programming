class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_cnt = Counter(s1)
        r = len(s1)
        l = 0
        for i in range(r , len(s2) + 1):
            if s1_cnt == Counter(s2[l:i]):
                return True
            l += 1
        return False
                  