class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s) +1)
        for start , end , dir in shifts:
            if dir == 1:
                diff[start] += 1
                diff[end+1] -= 1
            else:
                diff[start] -= 1
                diff[end+1] += 1
        for i in range(1 , len(diff)):
            diff[i] = diff[i] + diff[i-1]
        res = ''
        for j in range(len(s)):
            res += chr((ord(s[j]) - ord('a') + diff[j]) % 26 + ord('a'))
        return res