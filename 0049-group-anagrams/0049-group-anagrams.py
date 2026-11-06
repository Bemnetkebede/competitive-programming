class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans[(''.join((sorted(s))))].append(s)
        ans_ = []
        for val in ans.values():
            ans_.append(val)
        return ans_
        
        


            
        

        