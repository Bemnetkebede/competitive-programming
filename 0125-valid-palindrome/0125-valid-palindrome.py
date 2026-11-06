class Solution(object):
    def isPalindrome(self, s):
        alp = ''
        s=s.lower()
        for i in range(len(s)):
            if s[i].isalnum():
                alp += (s[i])
        return alp == alp[::-1]
        
         
        # if len(s) == 0:
        #    return True
        # else:
        #   start = 0
        #   s = s.lower()
        #   s.isalpnum()
        #   newS = re.sub(r"[^a-zA-Z0-9]","",s)
        #   print(newS)
        #   end = len(newS)-1
        #   while start < end:
        #     if newS[start] == newS[end]:
        #         start = start + 1
        #         end = end - 1
        #     else:
        #       return False
        #   return True
        