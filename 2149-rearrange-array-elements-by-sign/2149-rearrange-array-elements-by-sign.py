class Solution(object):
    def rearrangeArray(self, nums):
        pos , neg , all = [] , [],[]
        l , r=0 , 0
        for i in nums:
           if i > 0:
              pos.append(i)
           else:
               neg.append(i)
        
        while l < len(neg) and r < len(pos):
            all.append(pos[r])
            r += 1
            all.append(neg[l]) 
            l += 1 
        return all
             

        
        