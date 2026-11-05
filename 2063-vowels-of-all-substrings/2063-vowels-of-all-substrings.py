class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        dp = [0] * n
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(len(word)):
            if word[i] in vowels:
                dp[i] = dp[i-1] + ((i+1) * (n-i))
            else:
                dp[i] = dp[i-1]
        return dp[n-1] 
       