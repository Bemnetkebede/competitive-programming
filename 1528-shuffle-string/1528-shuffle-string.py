class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ''
        s = list(s)
        c = dict(sorted(zip(indices,s)))
        return ''.join(c.values())
    

           

       

       