class Solution(object):
    def firstPalindrome(self, words):
       l=0
       while l < len(words):
          if words[l] == words[l][::-1]:
            return words[l]
          else:
            l += 1
       return ""
            