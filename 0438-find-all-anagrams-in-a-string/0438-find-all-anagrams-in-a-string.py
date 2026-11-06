class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        res = []
        l = 0
        str_p = Counter(p)
        for i in range(len(s)-lp+1):
            str_s = Counter(s[l:l+lp])
            if str_p == str_s:
                res.append(l)
                l += 1
            else:
                l += 1


        return res

            
                
        


        