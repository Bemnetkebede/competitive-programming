class Solution(object):
    def appendCharacters(self, s, t):
        l, r = 0, 0
        
        # Iterate over both strings
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                r += 1  # Move to the next character in t when there's a match
            l += 1  # Always move to the next character in s
        
        # The characters left in t that weren't matched need to be appended
        return len(t) - r
        