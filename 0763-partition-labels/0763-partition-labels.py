class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        res = []
        for i , c in enumerate(s):
            last_idx[c] = i
        size , end = 0 , 0
        for j in range(len(s)):
            size += 1
            cur_end = last_idx[s[j]]
            end = max(end , cur_end)
            if j == end:
                res.append(size)
                size = 0
        return res


       





