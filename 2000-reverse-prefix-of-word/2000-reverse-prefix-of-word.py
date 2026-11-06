class Solution(object):
    def reversePrefix(self, word, ch):
        word = list(word)
        n = len(word)
        l = 0
        r = 0

        while r < n and word[r] != ch:
            r += 1

        if r < n: 
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1

        return ''.join(word)


        