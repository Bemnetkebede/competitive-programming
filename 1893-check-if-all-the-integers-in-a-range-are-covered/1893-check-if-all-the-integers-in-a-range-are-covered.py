class Solution(object):
    def isCovered(self, ranges, left, right):
        num_set = set()
        for i in range(len(ranges)):
            for j in range(ranges[i][0] , (ranges[i][1])+1):
                num_set.add(j)   
                
        for i in range(left , right + 1):
            if i not in num_set:
                return False
        return True
                

            
