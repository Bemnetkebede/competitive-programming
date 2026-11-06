from collections import Counter
class Solution(object):
    def areOccurrencesEqual(self, s):
        s = Counter(s)
        mx = max(s.values())
        for v in s.values():
            if v != mx:
                return False
        return True

            

        

        
        
        