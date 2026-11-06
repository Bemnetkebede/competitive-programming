class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse = True)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i 
        else:
            return len(citations)    
        



            
       
        