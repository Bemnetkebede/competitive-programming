class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        j = 0
        window = {}
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            max_freq = max(window.values())
            if ((right - j + 1) - max_freq) > k:
                window[s[j]] -= 1
                j += 1
            else:
                max_len = max(max_len , right - j + 1)

        return max_len
        

        